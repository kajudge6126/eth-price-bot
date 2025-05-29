import requests
import json
from telegram.ext import Updater, CommandHandler
import logging
import os

# === LOGGING ===
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# === CONFIGURATION ===
MEXC_API_URL = "https://www.mexc.com/api/v1/market/ticker?market=ETH_USDT"
TELEGRAM_API_KEY = os.getenv("TELEGRAM_API_KEY")

if not TELEGRAM_API_KEY:
    raise ValueError("TELEGRAM_API_KEY çevresel değişkeni tanımlanmadı.")

# === TELEGRAM BOT ===
def fiyat(update, context):
    try:
        response = requests.get(MEXC_API_URL)
        response.raise_for_status()

        data = response.json()
        price = data['data']['last']

        context.bot.send_message(chat_id=update.effective_chat.id, text=f"💱 ETH/USDT fiyatı: {price} USDT")
    except requests.RequestException as e:
        logger.error(f"API hatası: {e}")
        context.bot.send_message(chat_id=update.effective_chat.id, text="⚠️ MEXC API'sine erişilemiyor.")
    except KeyError:
        logger.error("Yanıt formatı beklenenden farklı.")
        context.bot.send_message(chat_id=update.effective_chat.id, text="⚠️ Fiyat bilgisi alınamadı.")

def main():
    updater = Updater(token=TELEGRAM_API_KEY, use_context=True)
    dp = updater.dispatcher
    
    dp.add_handler(CommandHandler("fiyat", fiyat))

    updater.start_polling()
    logger.info("Bot başlatıldı.")
    updater.idle()

if __name__ == "__main__":
    main()

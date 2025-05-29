# ETH/USDT Fiyat Botu – MEXC API + Telegram

Bu bot, Telegram üzerinden `/fiyat` komutu ile MEXC borsasından anlık ETH/USDT fiyat bilgisi sağlar.

## Özellikler

- MEXC API üzerinden anlık veri çekimi
- Komutla tetiklenen mesajlaşma
- Temel hata yönetimi

## Kurulum

1. Python bağımlılıklarını yükleyin:
    ```bash
    pip install python-telegram-bot requests
    ```

2. Ortam değişkenlerini ayarlayın:
    ```bash
    export TELEGRAM_API_KEY=your_bot_api_key
    ```

3. Botu çalıştırın:
    ```bash
    python eth_price_bot.py
    ```

## Güvenlik

API anahtarınızı açıkça paylaşmayın. `.env` dosyası kullanımı tavsiye edilir.

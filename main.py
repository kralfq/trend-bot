from telegram import bot
from flask import Flask
from threading import Thread
from telegram import Bot
import datetime
import time

app = Flask('')

# Web sunucusu için root endpoint
@app.route('/')
def home():
    return "ZYNTRUM BOT is alive!"

def run():
    app.run(host='0.0.0.0', port=8080)

# Sunucuyu arka planda başlat
def keep_alive():
    t = Thread(target=run)
    t.start()

# Telegram gönderim fonksiyonu
def send_daily_message():
    TOKEN = "7543256364:AAEUz9yFSpEk3O0K_xAZqZj95nWwaw3CIXs"
    CHAT_ID = "7887456007"
    bot = Bot(token=TOKEN)

    message = """
📊 ZYNTRUM – Trend Raporu
📅 6 Haziran 2025 – 10:00

🔥 TikTok'ta Patlayan Ürün:
🧽 Smart Cleaning Slippers
🔸 12M izlenme, 270K beğeni
🔸 Google Trends: +110%
🔸 Amazon: 5.600 satış / hafta

🎥 İçerik Önerisi:
"Bu terlikler süpürge gibi çalışıyor mu?" başlığı ile Reels paylaş.
    """

    while True:
        now = datetime.datetime.now()
        if now.hour == 8 and now.minute == 0:
            bot.send_message(chat_id=CHAT_ID, text=message)
            time.sleep(60)
        else:
            time.sleep(20)

# Hepsini başlat
keep_alive()
send_daily_message()

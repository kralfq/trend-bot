from flask import Flask
from threading import Thread
import datetime
import time
import os
from telegram import Bot

app = Flask(__name__)

@app.route('/')
def home():
    return "ZYNTRUM BOT is active!"

def run():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()

def send_daily_message():
    TOKEN = os.getenv("TELEGRAM_TOKEN")
    CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")
    bot = Bot(token=TOKEN)

    products = [
        {
            "title": "🧽 Smart Cleaning Slippers",
            "views": "12M izlenme",
            "likes": "270K beğeni",
            "trends": "+110%",
            "sales": "5.600 satış / hafta",
        },
        {
            "title": "📱 Magnetik Powerbank",
            "views": "9M izlenme",
            "likes": "150K beğeni",
            "trends": "+90%",
            "sales": "4.300 satış / hafta",
        },
        {
            "title": "🧊 Mini USB Fan",
            "views": "7M izlenme",
            "likes": "80K beğeni",
            "trends": "+70%",
            "sales": "3.200 satış / hafta",
        },
        {
            "title": "🎧 Bluetooth Gözlük",
            "views": "6M izlenme",
            "likes": "75K beğeni",
            "trends": "+65%",
            "sales": "2.800 satış / hafta",
        },
        {
            "title": "🧴 Otomatik Sabunluk",
            "views": "5M izlenme",
            "likes": "60K beğeni",
            "trends": "+55%",
            "sales": "2.500 satış / hafta",
        },
        {
            "title": "🖼️ Dijital Çerçeve",
            "views": "4M izlenme",
            "likes": "50K beğeni",
            "trends": "+45%",
            "sales": "2.200 satış / hafta",
        },
        {
            "title": "🔋 Akıllı Priz",
            "views": "3.5M izlenme",
            "likes": "40K beğeni",
            "trends": "+35%",
            "sales": "1.900 satış / hafta",
        }
    ]

    msg = f"📊 ZYNTRUM – Günlük Trend Raporu\n📅 {datetime.datetime.now().strftime('%d %B %Y – %H:%M')}\n\n"
    for p in products:
        msg += f"{p['title']}\n🔸 {p['views']}, {p['likes']}\n🔸 Google Trends: {p['trends']}\n🔸 Amazon: {p['sales']}\n\n"

    msg += "🎥 İçerik Fikri: 'Hangisi sizin favoriniz?' başlığıyla carousel Reels paylaş!"

while True:
    now = datetime.datetime.now()
    if now.minute == 8 and now.second == 0:
        send_daily_message()
        time.sleep(60)
    else:
        time.sleep(20)

keep_alive()
send_daily_message()
# GÜNLÜK Trend Mesajı Gönderimi
send_daily_message()




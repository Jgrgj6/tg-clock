from pyrogram import Client
import datetime
import asyncio
import pytz
from flask import Flask
from threading import Thread

# Veb-server (Koyeb o'chirib qo'ymasligi uchun)
app_web = Flask('')
@app_web.route('/')
def home(): return "I am alive"

def run_web():
    app_web.run(host='0.0.0.0', port=8080)

# Telegram ma'lumotlari
api_id = 37000758
api_hash = "c9d0005a174d34dd0d1ef5f5f104f927"
app = Client("my_session", api_id=api_id, api_hash=api_hash)

async def clock_loop():
    async with app:
        tashkent_tz = pytz.timezone('Asia/Tashkent')
        while True:
            now = datetime.datetime.now(tashkent_tz).strftime("%H:%M")
            try:
                await app.update_profile(first_name=f"ㅤㅤㅤ | {now}")
            except: pass
            # Keyingi daqiqa boshigacha kutish
            sleep_time = 60 - datetime.datetime.now(tashkent_tz).second
            await asyncio.sleep(sleep_time)

if __name__ == "__main__":
    Thread(target=run_web).start() 
    asyncio.run(clock_loop())
  

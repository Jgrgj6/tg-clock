from pyrogram import Client
import datetime
import asyncio
import pytz
from flask import Flask
from threading import Thread

# Koyeb serveri o'chib qolmasligi uchun kichik veb-server
app_web = Flask('')
@app_web.route('/')
def home(): return "I am alive"

def run_web():
    app_web.run(host='0.0.0.0', port=8080)

# MANA BU YERGA SEN YUBORGAN KODNI QO'YDIM
SESSION_STRING = "AgI0ljYACxMZypZgP9aHiIMoLLk9CFpxL_KSbwjxI_GzbLAmYSosxFx_-ICQnSeijK6Cm2vjbx94JP5ixc2fG7qPmjMpJ9f0v09eIoEINtDy79fhFI9PxB_8-x9b1YMgJpo1OWXPnz95uSsZCpmomIyvBwY_b8rpjnVCJx9E2lEcwHr8lN7-wABAQWkJXLO_GP1mFmWWYzCQ9cGe8hl3GyEqkhDJFt3i4Mw-1A9hagwZY4S0sNBCe6AeKH5LtZRHyVxsqp61EFMEAAD2a6Xd5MoORVIM37bRs_is7JM6XBuwJvDnMDoQkUj51En5ia1bVySN1S0pVdBqkWA4Q4nWbHwnuvoTHAAAAAGlsEvuAA"

api_id = 37000758
api_hash = "c9d0005a174d34dd0d1ef5f5f104f927"
app = Client("my_session", session_string=SESSION_STRING, api_id=api_id, api_hash=api_hash)

async def clock_loop():
    async with app:
        tashkent_tz = pytz.timezone('Asia/Tashkent')
        while True:
            # Vaqtni olish
            now = datetime.datetime.now(tashkent_tz).strftime("%H:%M")
            try:
                # Profil ismini yangilash
                await app.update_profile(first_name=f"ㅤㅤㅤ | {now}")
                print(f"Yangilandi: {now}")
            except Exception as e:
                print(f"Xatolik: {e}")
            
            # Keyingi daqiqagacha kutish
            sleep_time = 60 - datetime.datetime.now(tashkent_tz).second
            await asyncio.sleep(max(0, sleep_time))

if __name__ == "__main__":
    # Veb-serverni alohida oqimda ishga tushirish
    Thread(target=run_web).start() 
    
    # Yangi event loop yaratish (Python 3.11+ uchun xavfsiz yo'l)
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(clock_loop())
    

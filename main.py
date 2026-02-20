import asyncio
import datetime
import pytz
from pyrogram import Client
from flask import Flask
from threading import Thread

# Veb-server (Render o'chib qolmasligi uchun)
app_web = Flask('')
@app_web.route('/')
def home(): return "Bot is running!"

def run_web():
    app_web.run(host='0.0.0.0', port=8080)

# Sening sessiya koding
SESSION_STRING = "AgI0ljYACxMZypZgP9aHiIMoLLk9CFpxL_KSbwjxI_GzbLAmYSosxFx_-ICQnSeijK6Cm2vjbx94JP5ixc2fG7qPmjMpJ9f0v09eIoEINtDy79fhFI9PxB_8-x9b1YMgJpo1OWXPnz95uSsZCpmomIyvBwY_b8rpjnVCJx9E2lEcwHr8lN7-wABAQWkJXLO_GP1mFmWWYzCQ9cGe8hl3GyEqkhDJFt3i4Mw-1A9hagwZY4S0sNBCe6AeKH5LtZRHyVxsqp61EFMEAAD2a6Xd5MoORVIM37bRs_is7JM6XBuwJvDnMDoQkUj51En5ia1bVySN1S0pVdBqkWA4Q4nWbHwnuvoTHAAAAAGlsEvuAA"
api_id = 37000758
api_hash = "c9d0005a174d34dd0d1ef5f5f104f927"

async def clock_loop():
    app = Client("my_session", session_string=SESSION_STRING, api_id=api_id, api_hash=api_hash)
    await app.start()
    print("Bot muvaffaqiyatli ishga tushdi!")
    
    tashkent_tz = pytz.timezone('Asia/Tashkent')
    while True:
        now = datetime.datetime.now(tashkent_tz).strftime("%H:%M")
        try:
            # Profilni yangilash
            await app.update_profile(first_name=f"ㅤㅤㅤ | {now}")
            print(f"Yangilandi: {now}")
        except Exception as e:
            print(f"Yangilashda xato: {e}")
            
        # Keyingi daqiqagacha kutish
        await asyncio.sleep(60)

if __name__ == "__main__":
    # Serverni yoqish
    Thread(target=run_web).start()
    
    # Python 3.10/3.11/3.14 uchun eng barqaror loop
    try:
        asyncio.run(clock_loop())
    except KeyboardInterrupt:
        pass

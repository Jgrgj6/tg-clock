import asyncio
import datetime
import pytz
from pyrogram import Client
from flask import Flask
from threading import Thread

# 1. Veb-server (Render uyquga ketmasligi uchun)
app_web = Flask('')
@app_web.route('/')
def home(): 
    return "Bot is running 24/7 with perfect sync!"

def run_web():
    # Render uchun 8080 porti shart
    app_web.run(host='0.0.0.0', port=8080)

# 2. Sening ma'lumotlaring
SESSION_STRING = "AgI0ljYACxMZypZgP9aHiIMoLLk9CFpxL_KSbwjxI_GzbLAmYSosxFx_-ICQnSeijK6Cm2vjbx94JP5ixc2fG7qPmjMpJ9f0v09eIoEINtDy79fhFI9PxB_8-x9b1YMgJpo1OWXPnz95uSsZCpmomIyvBwY_b8rpjnVCJx9E2lEcwHr8lN7-wABAQWkJXLO_GP1mFmWWYzCQ9cGe8hl3GyEqkhDJFt3i4Mw-1A9hagwZY4S0sNBCe6AeKH5LtZRHyVxsqp61EFMEAAD2a6Xd5MoORVIM37bRs_is7JM6XBuwJvDnMDoQkUj51En5ia1bVySN1S0pVdBqkWA4Q4nWbHwnuvoTHAAAAAGlsEvuAA"
api_id = 37000758
api_hash = "c9d0005a174d34dd0d1ef5f5f104f927"

async def clock_loop():
    # ipv6=True bulutli serverlar uchun ulanishni barqaror qiladi
    app = Client("my_session", session_string=SESSION_STRING, api_id=api_id, api_hash=api_hash, ipv6=True)
    await app.start()
    print("✅ Bot serverda muvaffaqiyatli ishga tushdi!")
    
    tashkent_tz = pytz.timezone('Asia/Tashkent')
    
    while True:
        # Hozirgi aniq vaqtni olish
        now_dt = datetime.datetime.now(tashkent_tz)
        now_str = now_dt.strftime("%H:%M")
        
        try:
            # Profilni yangilash
            await app.update_profile(first_name=f"ㅤㅤㅤ | {now_str}")
            print(f"🕒 Yangilandi: {now_str}")
        except Exception as e:
            print(f"❌ Xato: {e}")
            
        # --- VAQTNI SINXRONLASH QISMI ---
        # Hozirgi sekundni aniqlaymiz
        current_sec = datetime.datetime.now(tashkent_tz).second
        
        # Keyingi daqiqa boshigacha (00-sekundgacha) qancha qolganini hisoblaymiz
        wait_time = 60 - current_sec
        
        # Agar vaqt 0 yoki undan kam bo'lib qolsa, 60 sekund kutamiz
        if wait_time <= 0:
            wait_time = 60
            
        # Bot keyingi daqiqa kirishi bilan uyg'onadi
        await asyncio.sleep(wait_time)

if __name__ == "__main__":
    # Veb-serverni alohida oqimda (background) yoqish
    server_thread = Thread(target=run_web)
    server_thread.daemon = True
    server_thread.start()
    
    # Asosiy asyncio loopni boshqarish (Python 3.10+ uchun)
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    try:
        loop.run_until_complete(clock_loop())
    except KeyboardInterrupt:
        pass

import requests
import schdule
import time

def ping():
    try:
        url = "https://creativehunt.onrender.com/"
        response = request.get(url)
        print(f"[+] Pinges at {time.ctime()}: status {response.status_code}")
    except Exception as e:
        print(f"[!] Error pinging: {e}")

schedule.every(5).minutes.do(ping_site)

print(" starting ping loop...")
while True:
    schedule.run_pedning()
    time.sleep(1)
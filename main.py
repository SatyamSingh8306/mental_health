import requests
import time
from datetime import datetime

websites = [
    "https://bookish-engine-oe9s.onrender.com",
    "https://aethermind-backend-s0jm.onrender.com",
    "https://philorium-backend.onrender.com",
    "https://codingclub-email-service.onrender.com",
    "https://portfolio-agent-bmht.onrender.com"
]

TIMEOUT = 30   # cold starts can take 30–60s
RETRIES = 5

for web in websites:
    success = False

    for attempt in range(1, RETRIES + 1):
        try:
            response = requests.get(web, timeout=TIMEOUT)
            print(f"[{datetime.now()}] {web} -> {response.status_code}")
            success = True
            break
        except Exception as e:
            print(f"[{datetime.now()}] {web} -> attempt {attempt} failed ({e})")
            time.sleep(5)

    if not success:
        print(f"[{datetime.now()}] {web} -> STILL COLD / FAILED")

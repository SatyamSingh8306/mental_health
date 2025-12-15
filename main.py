import requests
from datetime import datetime

websites = [
    "https://bookish-engine-oe9s.onrender.com",
    "https://aethermind-backend-s0jm.onrender.com",
    "https://philorium-backend.onrender.com",
    "https://codingclub-email-service.onrender.com",
    "https://portfolio-agent-bmht.onrender.com"
]

for web in websites:
    try:
        response = requests.get(web, timeout=10)
        print(f"[{datetime.now()}] {web} -> {response.status_code}")
    except Exception as e:
        print(f"[{datetime.now()}] {web} -> FAILED ({e})")

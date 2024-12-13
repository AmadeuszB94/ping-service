import time
import requests

def keep_alive():
    url = "https://tv-capital-webhook.onrender.com"  # Twój endpoint
    while True:
        try:
            response = requests.get(url)
            print(f"Pinged {url}, status code: {response.status_code}")
        except Exception as e:
            print(f"Error pinging {url}: {e}")
        time.sleep(30)  # Ping co 30 sekund

if __name__ == "__main__":
    keep_alive()

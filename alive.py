import requests, os

ASTRA_API_ENDPOINT = os.environ.get("ASTRA_API_ENDPOINT")
AUTH_TOKEN = os.environ.get("ASTRA_AUTH_TOKEN")

headers = {"x-cassandra-token": AUTH_TOKEN}

try:
    r = requests.get(ASTRA_API_ENDPOINT, headers=headers)
    print("Ping:", r.status_code, r.text[:100])  # print first 100 chars
except Exception as e:
    print("Error:", e)

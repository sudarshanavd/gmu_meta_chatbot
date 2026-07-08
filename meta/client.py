import os

import httpx
from dotenv import load_dotenv

load_dotenv()

ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
PHONE_NUMBER_ID = os.getenv("PHONE_NUMBER_ID")

META_URL = f"https://graph.facebook.com/v25.0/{PHONE_NUMBER_ID}/messages"

HEADERS = {
    "Authorization": f"Bearer {ACCESS_TOKEN}",
    "Content-Type": "application/json",
}


def _post_to_meta(payload: dict) -> httpx.Response:
    """POST a JSON payload to the Meta messages API."""
    with httpx.Client() as client:
        response = client.post(META_URL, headers=HEADERS, json=payload)
    print(f"Meta API [{response.status_code}]: {response.text}")
    return response

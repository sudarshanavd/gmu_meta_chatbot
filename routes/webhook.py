import pprint
from fastapi import APIRouter, Request
import os
from processors.webhook_processor import process_webhook_data

router = APIRouter(prefix="/webhook", tags=["webhook"])

VERIFY_TOKEN = os.getenv("VERIFY_TOKEN")

ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
PHONE_NUMBER_ID = os.getenv("PHONE_NUMBER_ID")

META_URL = f"https://graph.facebook.com/v25.0/{PHONE_NUMBER_ID}/messages"

# 🔹 1. Verification Endpoint (GET)
@router.get("")
async def verify_webhook(request: Request):
    params = request.query_params

    mode = params.get("hub.mode")
    token = params.get("hub.verify_token")
    challenge = params.get("hub.challenge")

    if mode == "subscribe" and token == VERIFY_TOKEN:
        return int(challenge)  # must return challenge
    return {"error": "Verification failed"}

@router.post("")
async def receive_message(request: Request):
    data = await request.json()
    # print("Received Webhook Data:", data)
    print("Received Webhook Data:")
    pprint.pprint(data)
    process_webhook_data(data)

    return {"status": "received"}
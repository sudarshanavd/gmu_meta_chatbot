import json

from handlers.message_handler import handle_incoming_message, _pending_forwarded_ids

# ── Admissions side-channel (non-blocking) ─────────────────────────────────
def _capture_admissions(message_data: dict):
    """Silently log student interest data. Never raises exceptions."""
    try:
        interest_code = (
            message_data.get("button_reply_id")
            or message_data.get("list_reply_id")
            or ""
        )
        wa_id = message_data.get("wa_id") or ""
        sender_name = message_data.get("sender_name") or ""
        phone = message_data.get("from") or wa_id
        if wa_id:
            from admissions.crud import upsert_student
            upsert_student(wa_id, sender_name, phone, interest_code)
    except Exception as exc:
        print(f"[Admissions] capture error (non-fatal): {exc}")


def _parse_flow_response(response_json):
    if not response_json:
        return {}

    try:
        parsed_response = json.loads(response_json)
    except json.JSONDecodeError:
        return {}

    return parsed_response if isinstance(parsed_response, dict) else {}


def process_webhook_data(data):
    """Extract useful WhatsApp webhook fields into a structured dict.

    Handles two webhook types:
      1. messages  – incoming user messages (text, interactive, etc.)
      2. statuses  – delivery status updates (sent, delivered, read, failed)
    """
    entry = data.get("entry", [])
    if not entry:
        return False

    first_entry = entry[0]
    changes = first_entry.get("changes", [])
    if not changes:
        return False

    first_change = changes[0]
    value = first_change.get("value", {})
    metadata = value.get("metadata", {})

    messages = value.get("messages", [])
    statuses = value.get("statuses", [])

    # ──────────────────────────────────────────
    #  STATUS webhook  (sent / delivered / read / failed)
    # ──────────────────────────────────────────
    if statuses:
        status_obj = statuses[0]
        pricing = status_obj.get("pricing", {})

        status_data = {
            "webhook_type": "status",
            "message_id": status_obj.get("id"),
            "recipient_id": status_obj.get("recipient_id"),
            "recipient_user_id": status_obj.get("recipient_user_id"),
            "status": status_obj.get("status"),          # sent | delivered | read | failed
            "timestamp": status_obj.get("timestamp"),
            # Pricing info
            "billable": pricing.get("billable"),
            "pricing_category": pricing.get("category"),
            "pricing_model": pricing.get("pricing_model"),
            "pricing_type": pricing.get("type"),
            # Metadata
            "messaging_product": value.get("messaging_product"),
            "display_phone_number": metadata.get("display_phone_number"),
            "phone_number_id": metadata.get("phone_number_id"),
        }

        # On "sent", re-key forwarded message ID: wa_id → template message ID
        if status_data["status"] == "sent":
            recipient = status_data["recipient_id"]
            template_msg_id = status_data["message_id"]
            if recipient in _pending_forwarded_ids:
                _pending_forwarded_ids[template_msg_id] = _pending_forwarded_ids.pop(recipient)
                print(f"🔗 Linked template {template_msg_id} → forwarded {_pending_forwarded_ids[template_msg_id]}")

        print(f"📨 Status update: {status_data['status']} for {status_data['message_id']}")
        return True

    # ──────────────────────────────────────────
    #  MESSAGE webhook  (text / interactive / media / etc.)
    # ──────────────────────────────────────────
    if messages:
        contacts = value.get("contacts", [])
        contact = contacts[0] if contacts else {}
        message = messages[0]

        # Normal text message structure
        text = message.get("text", {})

        # Reply context message structure
        context = message.get("context", {})

        # Interactive flow reply message structure
        interactive = message.get("interactive", {})
        nfm_reply = interactive.get("nfm_reply", {})
        flow_response_json = nfm_reply.get("response_json")

        # Interactive button reply message structure
        button_reply = interactive.get("button_reply", {})

        # Interactive list reply message structure
        list_reply = interactive.get("list_reply", {})

        message_data = {
            "webhook_type": "message",
            # Normal text message structure
            "sender_name": contact.get("profile", {}).get("name"),
            "wa_id": contact.get("wa_id"),
            "user_id": contact.get("user_id"),
            "from": message.get("from"),
            "from_user_id": message.get("from_user_id"),
            "message_id": message.get("id"),
            "message_type": message.get("type"),
            "text_body": text.get("body"),
            "timestamp": message.get("timestamp"),
            # Reply context message structure
            "context_from": context.get("from"),
            "context_message_id": context.get("id"),
            "forwarded": context.get("forwarded"),
            # Interactive flow reply message structure
            "interactive_type": interactive.get("type"),
            "flow_body": nfm_reply.get("body"),
            "flow_name": nfm_reply.get("name"),
            "flow_response_json": flow_response_json,
            "flow_response": _parse_flow_response(flow_response_json),
            # Interactive button reply message structure
            "button_reply_id": button_reply.get("id"),
            "button_reply_title": button_reply.get("title"),
            # Interactive list reply message structure
            "list_reply_id": list_reply.get("id"),
            "list_reply_title": list_reply.get("title"),
            "list_reply_description": list_reply.get("description"),
            # Metadata
            "messaging_product": value.get("messaging_product"),
            "display_phone_number": metadata.get("display_phone_number"),
            "phone_number_id": metadata.get("phone_number_id"),
        }

        print("Extracted webhook payload into message_data:", message_data)
        _capture_admissions(message_data)   # ← admissions side-channel
        handle_incoming_message(message_data)
        return True

    return False

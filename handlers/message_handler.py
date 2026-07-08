from meta.send_main import ( send_read_and_typing,
                               send_main_reply,
                               send_main_details,
                               send_program_details,
                               send_school_details,
                               send_branch_details,
                               send_course_details
                               )

# Holds the forwarded message ID per user until the flow reply arrives
_pending_forwarded_ids: dict[str, str] = {}


# ──────────────────────────────────────────────────────
#  Single sequential pipeline per message
# ──────────────────────────────────────────────────────
def _process_message(message_data: dict):
    """Task-per-message: runs all steps sequentially for one incoming message."""
    message_id = message_data.get("message_id")
    wa_id = message_data.get("wa_id")
    message_type = message_data.get("message_type")
    button_reply_id = message_data.get("button_reply_id") or ""
    list_reply_id = message_data.get("list_reply_id") or ""
    print(button_reply_id,list_reply_id)

    # ── Step 1: Read receipt / indicator ───────────────
    if message_id:
        send_read_and_typing(message_id)
        print(f"Sent read receipt + typing for message")

    # ── Step 2: Forwarded → store ID + send flow ──────
    if message_type == "text" :
        send_main_reply(wa_id)
        return
    
    if len(button_reply_id) == 1 or len(list_reply_id) == 1:
            send_main_details(wa_id,button_reply_id)
            return
    
    if len(list_reply_id) == 2 or len(button_reply_id) == 2:
            send_program_details(wa_id,list_reply_id)
            return
    if len(button_reply_id) == 3 or len(list_reply_id) == 3:
            send_school_details(wa_id,button_reply_id)
            return
    if len(list_reply_id) == 4 or len(button_reply_id) == 4:
            print("hi")
            send_branch_details(wa_id,list_reply_id)
            return
    if len(button_reply_id) == 5 or len(list_reply_id) == 5:
            send_course_details(wa_id,button_reply_id)
            return
    else :
          send_main_reply(wa_id)
          return
    
# ──────────────────────────────────────────────────────
#  Public entry point (called from webhook processor)
# ──────────────────────────────────────────────────────
def handle_incoming_message(message_data: dict):
    """Handles the incoming message pipeline sequentially."""
    sender_name = message_data.get("sender_name")
    text_body = message_data.get("text_body")
    print(f"Message from {sender_name}: {text_body}")

    _process_message(message_data)

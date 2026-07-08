from schema.indicator_schema import MarkAsReadWithTyping
from payload.main_payload import build_main_reply_payload
from payload.ug import ug_payload
from payload.pg import pg_payload
from meta.client import _post_to_meta
from payload.website import build_website_payload


def send_read_and_typing(message_id: str):
    """Send blue tick ✓✓ + typing indicator for the given message."""
    payload = MarkAsReadWithTyping(message_id=message_id)
    return _post_to_meta(payload.model_dump())


def send_main_reply(wa_id: str):
    """Send the GMU form as a threaded response to the user's message."""
    payload = build_main_reply_payload(wa_id)
    return _post_to_meta(payload)

def send_main_details(wa_id: str, button_reply_id: str):
    """Send the main details based on the button reply ID."""
    if button_reply_id == "a":
        payload = ug_payload.build_ug_details_payload(wa_id)
    elif button_reply_id == "b":
        payload = pg_payload.build_pg_details_payload(wa_id)
    elif button_reply_id == "c":
        payload = build_website_payload(wa_id)
    else:
        raise ValueError("Invalid button reply ID for main details.")
    
    return _post_to_meta(payload)
    
def send_program_details(wa_id: str, list_reply_id: str):
    """Send the program details based on the list reply ID."""
    if list_reply_id[0] == "a":
        from meta.ug.send_ug import send_aX_details

        send_aX_details(wa_id,list_reply_id)
    elif list_reply_id[0] == "b":
        from meta.pg.send_pg import send_bX_details

        send_bX_details(wa_id,list_reply_id)
    else:
        raise ValueError("Invalid list reply ID for program details.")
    
def send_school_details(wa_id: str, button_reply_id: str):
    """Send the school details based on the button reply ID."""
    if button_reply_id[0] == "a":
        from meta.ug.send_ug import send_aXX_details

        send_aXX_details(wa_id,button_reply_id)
    elif button_reply_id[0] == "b":
        from meta.pg.send_pg import send_bXX_details

        send_bXX_details(wa_id,button_reply_id)
    else:
        raise ValueError("Invalid button reply ID for school details.")
    
def send_branch_details(wa_id: str, list_reply_id: str):
    """Send the branch details based on the list reply ID."""
    if list_reply_id[0] == "a":
        from meta.ug.send_ug import send_aXXX_details
        print("2")
        send_aXXX_details(wa_id,list_reply_id)
    elif list_reply_id[0] == "b":
        from meta.pg.send_pg import send_bXXX_details

        send_bXXX_details(wa_id,list_reply_id)
    else:
        raise ValueError("Invalid list reply ID for branch details.")
    
def send_course_details(wa_id: str, button_reply_id: str):
    """Send the course details based on the button reply ID."""
    if button_reply_id[0] == "a":
        from meta.ug.send_ug import send_aXXXX_details

        send_aXXXX_details(wa_id,button_reply_id)
    elif button_reply_id[0] == "b":
        from meta.pg.send_pg import send_bXXXX_details

        send_bXXXX_details(wa_id,button_reply_id)
    else:
        raise ValueError("Invalid button reply ID for course details.")

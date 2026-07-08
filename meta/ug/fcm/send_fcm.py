from meta.client import _post_to_meta
from payload.ug.fet import fet_payload
# from meta.ug.fcit. import send_abaX_details, send_abaXX_details    
from payload.ug.fcm import *
from meta.ug.fcm.sc.send_sc import send_abaX_details,send_abaXX_details
from meta.ug.fcm.sm.send_sm import send_abbX_details,send_abbXX_details

def send_abX_details(wa_id: str, button_reply_id: str):
    """Send the details for the first school option based on the button reply ID."""
    if button_reply_id[2] == "a":
        payload = sc_payload.build_school_of_commerce_payload(wa_id)
    elif button_reply_id[2] == "b":
        payload = sm_payload.build_school_of_management_payload(wa_id)
    return _post_to_meta(payload)

def send_abXX_details(wa_id: str, button_reply_id: str):
    """Send the details for the first branch option based on the button reply ID."""
    if button_reply_id[2] == "a":
        send_abaX_details(wa_id, button_reply_id)
    elif button_reply_id[2] == "b":
        send_abbX_details(wa_id, button_reply_id)

def send_abXXX_details(wa_id: str, button_reply_id: str):
    """Send the details for the first course option based on the button reply ID."""
    if button_reply_id[2] == "a":
        send_abaXX_details(wa_id, button_reply_id)
    elif button_reply_id[2] == "b":
        send_abbXX_details(wa_id, button_reply_id)

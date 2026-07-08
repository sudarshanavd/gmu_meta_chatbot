from meta.client import _post_to_meta
from payload.ug.fet import fet_payload
from meta.ug.fet.scst.send_scst import send_aaaX_details,send_aaaXX_details
from meta.ug.fet.se.send_se import send_aabX_details,send_aabXX_details
from payload.ug.fet import *

def send_aaX_details(wa_id: str, button_reply_id: str):
    """Send the details for the first school option based on the button reply ID."""
    if button_reply_id[2] == "a":
        payload = scst_payload.build_cs_technology_list_payload(wa_id)
    elif button_reply_id[2] == "b":
        payload = se_payload.build_school_of_engineering_payload(wa_id)
    return _post_to_meta(payload)

def send_aaXX_details(wa_id: str, button_reply_id: str):
    """Send the details for the first branch option based on the button reply ID."""
    if button_reply_id[2] == "a":
        send_aaaX_details(wa_id, button_reply_id)
    elif button_reply_id[2] == "b":
        send_aabX_details(wa_id, button_reply_id)

def send_aaXXX_details(wa_id: str, button_reply_id: str):
    """Send the details for the first course option based on the button reply ID."""
    if button_reply_id[2] == "a":
        send_aaaXX_details(wa_id, button_reply_id)
    elif button_reply_id[2] == "b":
        send_aabXX_details(wa_id, button_reply_id)

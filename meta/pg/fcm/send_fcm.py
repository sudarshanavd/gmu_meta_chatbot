from meta.client import _post_to_meta
from payload.pg.fcm import *
from meta.pg.fcm.sc.send_sc import (send_bdaX_details,
                                    send_bdaXX_details)

def send_bdX_details(wa_id: str, button_reply_id: str):
    """Send the details for the first school option based on the button reply ID."""
    if button_reply_id[2] == "a":
        payload = fcm_payload.build_pg_fcm_payload(wa_id)
    return _post_to_meta(payload)

def send_bdXX_details(wa_id: str, button_reply_id: str):
    """Send the details for the first branch option based on the button reply ID."""
    if button_reply_id[2] == "a":
        send_bdaX_details(wa_id, button_reply_id)
    
def send_bdXXX_details(wa_id: str, button_reply_id: str):
    """Send the details for the first course option based on the button reply ID."""
    if button_reply_id[2] == "a":
        send_bdaXX_details(wa_id, button_reply_id)
   
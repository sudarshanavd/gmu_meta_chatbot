from meta.client import _post_to_meta
from payload.pg.fcit import *
from meta.pg.fcit.sca.send_sca import (send_bcaX_details,
                                       send_bcaXX_details)

def send_bcX_details(wa_id: str, button_reply_id: str):
    """Send the details for the first school option based on the button reply ID."""
    if button_reply_id[2] == "a" or button_reply_id[2] == "b":
        payload = sca_payload.build_pg_school_of_computer_application_payload(wa_id)
    return _post_to_meta(payload)

def send_bcXX_details(wa_id: str, button_reply_id: str):
    """Send the details for the first branch option based on the button reply ID."""
    if button_reply_id[2] == "a" or button_reply_id[2] == "b":
        print("Sending details for branch option...")
        send_bcaX_details(wa_id, button_reply_id)

def send_bcXXX_details(wa_id: str, button_reply_id: str):
    """Send the details for the first course option based on the button reply ID."""
    if button_reply_id[2] == "a" or button_reply_id[2] == "b":
        send_bcaXX_details(wa_id, button_reply_id)

    
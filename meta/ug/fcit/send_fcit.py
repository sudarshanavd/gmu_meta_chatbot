from meta.client import _post_to_meta
from payload.ug.fet import fet_payload
# from meta.fet.scst.send_message import send_adaX_details, send_adaXX_details    
from payload.ug.fcit import *
from meta.ug.fcit.sca.send_sca import (send_aeaX_details,
                                       send_aeaXX_details,
                                       )
from meta.ug.fcit.scs.send_scs import (send_aebX_details,
                                       send_aebXX_details)

def send_aeX_details(wa_id: str, button_reply_id: str):
    """Send the details for the first school option based on the button reply ID."""
    if button_reply_id[2] == "a":
        payload = sca_payload.build_school_of_computer_application_payload(wa_id)
    elif button_reply_id[2] == "b":
        payload = scs_payload.build_school_of_computer_science_payload(wa_id)
    return _post_to_meta(payload)

def send_aeXX_details(wa_id: str, button_reply_id: str):
    """Send the details for the first branch option based on the button reply ID."""
    if button_reply_id[2] == "a":
        send_aeaX_details(wa_id, button_reply_id)
    elif button_reply_id[2] == "b":
        send_aebX_details(wa_id, button_reply_id)

def send_aeXXX_details(wa_id: str, button_reply_id: str):
    """Send the details for the first course option based on the button reply ID."""
    if button_reply_id[2] == "a":
        send_aeaXX_details(wa_id, button_reply_id)
    elif button_reply_id[2] == "b":
        send_aebXX_details(wa_id, button_reply_id)
    

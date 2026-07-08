from meta.client import _post_to_meta
from payload.ug.fcit.sca.sub import bca_payoad
from meta.ug.fcit.sca.sub import gen

def send_aeaX_details(wa_id, button_reply_id):
    """Send the details for the first course option based on the button reply ID."""
    if button_reply_id[3] == "a":
        payload = bca_payoad.build_bca_general_program_payload(wa_id)   
    
    return _post_to_meta(payload)

def send_aeaXX_details(wa_id, button_reply_id):
    """Send the details for the first course option based on the button reply ID."""
    if button_reply_id[3] == "a":
        gen.send_aeaaX_details(wa_id, button_reply_id)

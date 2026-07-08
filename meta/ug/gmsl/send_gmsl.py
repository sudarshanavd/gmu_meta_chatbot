from meta.client import _post_to_meta
from payload.ug.gmsl.sub import bbl_payload,bcl_payload,llb_payload
from meta.ug.gmsl.sub import send_bbl,send_bcl,send_llb

def send_acXX_details(wa_id, button_reply_id):
    """Send the details for the first course option based on the button reply ID."""
    if button_reply_id[3] == "a":
        payload = llb_payload.build_llb_program_payload(wa_id)
    elif button_reply_id[3] == "b":
        payload = bbl_payload.build_bballb_program_payload(wa_id)   
    elif button_reply_id[3] == "c":
        payload = bcl_payload.build_bcomllb_program_payload(wa_id)
    return _post_to_meta(payload)
    
def send_acXXX_details(wa_id, button_reply_id):
    if button_reply_id[3] == "a":
        send_acaXX_details(wa_id, button_reply_id)
    elif button_reply_id[3] == "b":
        send_acaXX_details(wa_id, button_reply_id)
    elif button_reply_id[3] == "c":
        send_acaXX_details(wa_id, button_reply_id)

def send_acaXX_details(wa_id, button_reply_id):
    if button_reply_id[3] == "a":
        send_llb.send_acaaX_details(wa_id, button_reply_id)

def send_acabXX_details(wa_id, button_reply_id):
    if button_reply_id[3] == "a":
        send_bbl.send_acabX_details(wa_id, button_reply_id)

def send_acaXX_details(wa_id, button_reply_id):
    if button_reply_id[3] == "a":
        send_bcl.send_acacX_details(wa_id, button_reply_id)
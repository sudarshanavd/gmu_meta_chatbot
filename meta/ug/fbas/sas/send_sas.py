from meta.client import _post_to_meta
from payload.ug.fbas.sas.sub import bte_payoad,fst_payoad,im_payoad
from meta.ug.fbas.sas.sub import bte,fst,im

def send_adcX_details(wa_id, button_reply_id):
    """Send the details for the first course option based on the button reply ID."""
    if button_reply_id[3] == "a":
        payload = fst_payoad.build_bsc_fst_program_payload(wa_id)   
    elif button_reply_id[3] == "b":
        payload = bte_payoad.build_bsc_bte_program_payload(wa_id)
    elif button_reply_id[3] == "c":
        payload = im_payoad.build_bsc_im_program_payload(wa_id) 
    
    return _post_to_meta(payload)

def send_adcXX_details(wa_id, button_reply_id):
    """Send the details for the first course option based on the button reply ID."""
    if button_reply_id[3] == "a":
        fst.send_adcaX_details(wa_id, button_reply_id)
    elif button_reply_id[3] == "b":
        bte.send_adcbX_details(wa_id, button_reply_id)
    elif button_reply_id[3] == "c":
        im.send_adccX_details(wa_id, button_reply_id)
    
   

from meta.client import _post_to_meta
from payload.ug.fbas.smps.sub import pm_payoad,scs_payoad,mcs_payoad
from meta.ug.fbas.smps.sub import mcs,pm,scs

def send_adaX_details(wa_id, button_reply_id):
    """Send the details for the first course option based on the button reply ID."""
    if button_reply_id[3] == "a":
        payload = pm_payoad.build_bsc_pm_program_payload(wa_id)   
    elif button_reply_id[3] == "b":
        payload = mcs_payoad.build_bsc_mcs_program_payload(wa_id)
    elif button_reply_id[3] == "c":
        payload = scs_payoad.build_bsc_scs_program_payload(wa_id) 
    return _post_to_meta(payload)

def send_adaXX_details(wa_id, button_reply_id):
    """Send the details for the first course option based on the button reply ID."""
    if button_reply_id[3] == "a":
        pm.send_adaaX_details(wa_id, button_reply_id)
    elif button_reply_id[3] == "b":
        mcs.send_adabX_details(wa_id, button_reply_id)
    elif button_reply_id[3] == "c":
        scs.send_adacX_details(wa_id, button_reply_id)
    
   

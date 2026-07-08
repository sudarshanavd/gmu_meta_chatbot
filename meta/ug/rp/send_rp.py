from meta.client import _post_to_meta
from payload.ug.rp.sub import fbas_payoad,fcit_payoad,fcm_payoad,fet_payoad
from meta.ug.rp.sub import fbas,fcit,fcm,fet

def send_afXX_details(wa_id, button_reply_id):
    """Send the details for the first course option based on the button reply ID."""
    if button_reply_id[3] == "a":
        payload = fet_payoad.build_phd_fet_program_payload(wa_id)
    elif button_reply_id[3] == "b":
        payload = fcit_payoad.build_phd_fcit_program_payload(wa_id)   
    elif button_reply_id[3] == "c":
        payload = fbas_payoad.build_phd_fcit_program_payload(wa_id)
    elif button_reply_id[3] == "d":
        payload = fcm_payoad.build_phd_fcm_program_payload(wa_id)
    return _post_to_meta(payload)
    
def send_afXXX_details(wa_id, button_reply_id):
    if button_reply_id[3] == "a":
        fet.send_afaaX_details(wa_id, button_reply_id)
    elif button_reply_id[3] == "b":
        fcit.send_afabX_details(wa_id, button_reply_id)
    elif button_reply_id[3] == "c":
        fbas.send_afacX_details(wa_id, button_reply_id)
    elif button_reply_id[3] == "d":
        fcm.send_afadX_details(wa_id, button_reply_id)

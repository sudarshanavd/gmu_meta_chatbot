from meta.client import _post_to_meta
from payload.pg.gmbs.sub import mbaa_payoad,mbag_payoad,mbai_payoad,mbap_payoad
from meta.pg.gbs.sub import adv,gen,int,pro

def send_beXX_details(wa_id, button_reply_id):
    """Send the details for the first course option based on the button reply ID."""
    if button_reply_id[3] == "a":
        payload = mbag_payoad.build_mba_program_payload(wa_id)
    elif button_reply_id[3] == "b":
        payload = mbap_payoad.build_mba_professional_program_payload(wa_id)   
    elif button_reply_id[3] == "c":
        payload = mbaa_payoad.build_mba_advanced_program_payload(wa_id)
    elif button_reply_id[3] == "d":
        payload = mbai_payoad.build_mba_international_program_payload(wa_id)
    return _post_to_meta(payload)
    
def send_beXXX_details(wa_id, button_reply_id):
    if button_reply_id[3] == "a":
        gen.send_beaaX_details(wa_id, button_reply_id)
    elif button_reply_id[3] == "b":
        pro.send_beabX_details(wa_id, button_reply_id)
    elif button_reply_id[3] == "c":
        adv.send_beacX_details(wa_id, button_reply_id)
    elif button_reply_id[3] == "d":
        int.send_beacX_details(wa_id, button_reply_id)
    


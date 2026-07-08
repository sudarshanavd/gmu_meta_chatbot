from meta.client import _post_to_meta
from payload.pg.fbas.sub import mscft_payoad,mscc_payoad,mscm_payoad,mscp_payoad
from meta.pg.fbas.sub import che,ftech,math,phy

def send_bbXX_details(wa_id, button_reply_id):
    """Send the details for the first course option based on the button reply ID."""
    if button_reply_id[3] == "a":
        payload = mscp_payoad.build_msc_physics_program_payload(wa_id)
    elif button_reply_id[3] == "b":
        payload = mscc_payoad.build_msc_chemistry_program_payload(wa_id)   
    elif button_reply_id[3] == "c":
        payload = mscm_payoad.build_msc_mathematics_program_payload(wa_id)
    elif button_reply_id[3] == "d":
        payload = mscft_payoad.build_msc_food_technology_program_payload(wa_id)
    return _post_to_meta(payload)
    
def send_bbXXX_details(wa_id, button_reply_id):
    if button_reply_id[3] == "a":
        phy.send_bbaaX_details(wa_id, button_reply_id)
    elif button_reply_id[3] == "b":
        che.send_bbabX_details(wa_id, button_reply_id)
    elif button_reply_id[3] == "c":
        math.send_bbacX_details(wa_id, button_reply_id)
    elif button_reply_id[3] == "c":
        ftech.send_bbadX_details(wa_id, button_reply_id)

from meta.client import _post_to_meta
from payload.ug.fbas.scbs.sub import cb_payoad,ccs_payoad,ces_payoad,cz_payoad,pc_payoad
from meta.ug.fbas.scbs.sub import cb,ccs,ces,cz,pc

def send_adbX_details(wa_id, button_reply_id):
    """Send the details for the first course option based on the button reply ID."""
    if button_reply_id[3] == "a":
        payload = pc_payoad.build_bsc_pc_program_payload(wa_id)   
    elif button_reply_id[3] == "b":
        payload = ccs_payoad.build_bsc_ccs_program_payload(wa_id)
    elif button_reply_id[3] == "c":
        payload = cz_payoad.build_bsc_cz_program_payload(wa_id) 
    elif button_reply_id[3] == "d":
        payload = cb_payoad.build_bsc_cb_program_payload(wa_id) 
    elif button_reply_id[3] == "e":
        payload = ces_payoad.build_bsc_ces_program_payload(wa_id)
    return _post_to_meta(payload)

def send_adbXX_details(wa_id, button_reply_id):
    """Send the details for the first course option based on the button reply ID."""
    if button_reply_id[3] == "a":
        pc.send_adbaX_details(wa_id, button_reply_id)
    elif button_reply_id[3] == "b":
        ccs.send_adbbX_details(wa_id, button_reply_id)
    elif button_reply_id[3] == "c":
        cz.send_adbcX_details(wa_id, button_reply_id)
    elif button_reply_id[3] == "d":
        cb.send_adbdX_details(wa_id, button_reply_id)  
    elif button_reply_id[3] == "e":
        ces.send_adbeX_details(wa_id, button_reply_id) 
   

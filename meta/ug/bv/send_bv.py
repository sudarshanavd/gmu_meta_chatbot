from meta.client import _post_to_meta
from payload.ug.bv.sub import bvagss_payoad,bvave_payoad,bvdd_payoad,bvecdm_payoad,bvevt_payoad,bvfdam_payoad
from meta.ug.bv.sub import agss,ave,dda,ecdm,evt,fdam

def send_agXX_details(wa_id, button_reply_id):
    """Send the details for the first course option based on the button reply ID."""
    if button_reply_id[3] == "a":
        payload = bvevt_payoad.build_bvoc_evt_program_payload(wa_id)
    elif button_reply_id[3] == "b":
        payload = bvfdam_payoad.build_bvoc_fdam_program_payload(wa_id)   
    elif button_reply_id[3] == "c":
        payload = bvdd_payoad.build_bvoc_dda_program_payload(wa_id)
    elif button_reply_id[3] == "d":
        payload = bvagss_payoad.build_bvoc_agss_program_payload(wa_id)
    elif button_reply_id[3] == "e":
        payload = bvecdm_payoad.build_bvoc_ecdm_program_payload(wa_id)
    elif button_reply_id[3] == "f":
        payload = bvave_payoad.build_bsc_ave_program_payload(wa_id)
    return _post_to_meta(payload)
    
def send_agXXX_details(wa_id, button_reply_id):
    if button_reply_id[3] == "a":
        evt.send_agaaX_details(wa_id, button_reply_id)
    elif button_reply_id[3] == "b":
        fdam.send_agabX_details(wa_id, button_reply_id)
    elif button_reply_id[3] == "c":
        dda.send_agacX_details(wa_id, button_reply_id)
    elif button_reply_id[3] == "d":
        agss.send_agadX_details(wa_id, button_reply_id)
    elif button_reply_id[3] == "e":
        ecdm.send_agaeX_details(wa_id, button_reply_id)
    elif button_reply_id[3] == "f":
        ave.send_agaeX_details(wa_id, button_reply_id)


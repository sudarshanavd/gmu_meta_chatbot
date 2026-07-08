from meta.client import _post_to_meta
from meta.ug.fet.scst.sub import send_cse,send_ise,send_aiml,send_bs,send_iot,send_ds,send_cy,send_cc,send_iy
from payload.ug.fet.scst.sub import cse_payoad,ise_payload,aiml_payoad,ai_bbs_payoad,iot_payoad,ds_payoad,cy_payoad,cc_payoad,iy_payoad

def send_aaaX_details(wa_id, button_reply_id):
    """Send the details for the first course option based on the button reply ID."""
    if button_reply_id[3] == "a":
        print("here")
        payload = cse_payoad.build_cse_program_payload(wa_id)
    elif button_reply_id[3] == "b":
        payload = ise_payload.build_ise_program_payload(wa_id)
    elif button_reply_id[3] == "c":
        payload = aiml_payoad.build_aiml_program_payload(wa_id)
    elif button_reply_id[3] == "d":
        payload = ai_bbs_payoad.build_cs_aibcbs_program_payload(wa_id)
    elif button_reply_id[3] == "e":
        payload = iot_payoad.build_iot_program_payload(wa_id) 
    elif button_reply_id[3] == "f":
        payload = ds_payoad.build_ds_program_payload(wa_id) 
    elif button_reply_id[3] == "g":
        payload = cy_payoad.build_cy_program_payload(wa_id)
    elif button_reply_id[3] == "h":
        payload = cc_payoad.build_cc_program_payload(wa_id)
    elif button_reply_id[3] == "i":
        payload = iy_payoad.build_iy_program_payload(wa_id)
    return _post_to_meta(payload)

def send_aaaXX_details(wa_id, button_reply_id):
    """Send the details for the first course option based on the button reply ID."""
    if button_reply_id[3] == "a":
        send_cse.send_aaaaX_details(wa_id, button_reply_id)
    elif button_reply_id[3] == "b":
        send_ise.send_aaabX_details(wa_id, button_reply_id)
    elif button_reply_id[3] == "c":
        send_aiml.send_aaacX_details(wa_id, button_reply_id)
    elif button_reply_id[3] == "d":
        send_bs.send_aaadX_details(wa_id, button_reply_id)
    elif button_reply_id[3] == "e":
        send_iot.send_aaaeX_details(wa_id, button_reply_id) 
    elif button_reply_id[3] == "f":
        send_ds.send_aaafX_details(wa_id, button_reply_id) 
    elif button_reply_id[3] == "g":
        send_cy.send_aaagX_details(wa_id, button_reply_id) 
    elif button_reply_id[3] == "h":
        send_cc.send_aaahX_details(wa_id, button_reply_id) 
    elif button_reply_id[3] == "i":
        send_iy.send_aaaiX_details(wa_id, button_reply_id)      

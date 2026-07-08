from meta.client import _post_to_meta
from payload.ug.fcm.sm.sub import (aba_payload,
                                   am_payload,
                                   bf_payload,
                                   dm_payload,
                                   gen_payload,
                                   hm_payload,
                                   them_payload)
from meta.ug.fcm.sm.sub import (send_aiba,
                                send_am,
                                send_bf,
                                send_dmec,
                                send_gen,
                                send_hm,
                                send_them)

def send_abbX_details(wa_id, button_reply_id):
    """Send the details for the first course option based on the button reply ID."""
    if button_reply_id[3] == "a":
        payload = gen_payload.build_bba_general_program_payload(wa_id)   
    elif button_reply_id[3] == "b":
        payload = bf_payload.build_bf_program_payload(wa_id)
    elif button_reply_id[3] == "c":
        payload = aba_payload.build_aba_program_payload(wa_id) 
    elif button_reply_id[3] == "d":
        payload = dm_payload.build_dme_program_payload(wa_id) 
    elif button_reply_id[3] == "e":
        payload = am_payload.build_am_program_payload(wa_id) 
    elif button_reply_id[3] == "f":
        payload = them_payload.build_them_program_payload(wa_id) 
    elif button_reply_id[3] == "g":
        payload = them_payload.build_cse_program_payload(wa_id)
    return _post_to_meta(payload)

def send_abbXX_details(wa_id, button_reply_id):
    """Send the details for the first course option based on the button reply ID."""
    if button_reply_id[3] == "a":
        send_gen.send_abbaX_details(wa_id, button_reply_id)
    elif button_reply_id[3] == "b":
        send_bf.send_abbbX_details(wa_id, button_reply_id)
    elif button_reply_id[3] == "c":
        send_aiba.send_abbcX_details(wa_id, button_reply_id)
    elif button_reply_id[3] == "d":
        send_dmec.send_abbdX_details(wa_id, button_reply_id)  
    elif button_reply_id[3] == "e":
        send_am.send_abbeX_details(wa_id, button_reply_id) 
    elif button_reply_id[3] == "f":
        send_them.send_abbfX_details(wa_id, button_reply_id) 
    elif button_reply_id[3] == "g":
        send_hm.send_abbgX_details(wa_id, button_reply_id)      
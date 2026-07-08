from meta.client import _post_to_meta
from payload.ug.fcm.sc.sub import aba_payoad,at_payoad,dabi_payoad,gen_payload
from payload.ug.fet.scst.sub import *
from meta.ug.fcm.sc.sub import send_aiba,send_at,send_dabi,send_gen

def send_abaX_details(wa_id, button_reply_id):
    """Send the details for the first course option based on the button reply ID."""
    if button_reply_id[3] == "a":
        payload = gen_payload.build_bcom_general_program_payload(wa_id)
    elif button_reply_id[3] == "b":
        payload = dabi_payoad.build_dabi_program_payload(wa_id)   
    elif button_reply_id[3] == "c":
        payload = aba_payoad.build_aba_program_payload(wa_id)
    elif button_reply_id[3] == "d":
        payload = at_payoad.build_at_program_payload(wa_id) 
    return _post_to_meta(payload)

def send_abaXX_details(wa_id, button_reply_id):
    """Send the details for the first course option based on the button reply ID."""
    if button_reply_id[3] == "a":
        send_gen.send_abaaX_details(wa_id, button_reply_id)
    elif button_reply_id[3] == "b":
        send_dabi.send_ababX_details(wa_id, button_reply_id)
    elif button_reply_id[3] == "c":
        send_aiba.send_abacX_details(wa_id, button_reply_id)
    elif button_reply_id[3] == "d":
        send_at.send_abadX_details(wa_id, button_reply_id)       

from meta.client import _post_to_meta
from payload.pg.fcm.sc.sub import mafdb_payoad,mfae_payoad
from meta.pg.fcm.sc.sub import afdb,fae

def send_bdaX_details(wa_id, button_reply_id):
    """Send the details for the first course option based on the button reply ID."""
    if button_reply_id[3] == "a":
        payload = mafdb_payoad.build_mcom_afdb_program_payload(wa_id)     
    elif button_reply_id[3] == "b":
        payload = mfae_payoad.build_mcom_fae_program_payload(wa_id)  

    return _post_to_meta(payload)

def send_bdaXX_details(wa_id, button_reply_id):
    """Send the details for the first course option based on the button reply ID."""
    if button_reply_id[3] == "a":
        afdb.send_bdaaX_details(wa_id, button_reply_id)
    elif button_reply_id[3] == "b":
        fae.send_bdabX_details(wa_id, button_reply_id)
   

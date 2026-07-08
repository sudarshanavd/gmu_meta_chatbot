from meta.client import _post_to_meta
from payload.pg import *
from meta.pg.fcit.send_fcit import send_bcX_details
from meta.pg.fcm.send_fcm import send_bdX_details,send_bdXX_details,send_bdXXX_details
from meta.pg.fcit.send_fcit import send_bcX_details,send_bcXX_details,send_bcXXX_details
from meta.pg.gmsas.send_gmsas import send_baXX_details,send_baXXX_details
from meta.pg.fbas.send_fbas import send_bbXX_details,send_bbXXX_details
from meta.pg.gbs.send_gbs import send_beXX_details,send_beXXX_details
from meta.pg.pgd.send_pgd import send_bfXX_details,send_bfXXX_details

def send_bX_details(wa_id: str, list_reply_id: str):
    """Send the details for the first program option based on the list reply ID."""
    if list_reply_id[1] == "a":
        payload = gmsas_payload.build_gmsas_payload(wa_id)
    elif list_reply_id[1] == "b":
        payload = fbas_payload.build_pg_fbas_payload(wa_id)
    elif list_reply_id[1] == "c":
        payload = fcit_payload.build_pg_fcit_payload(wa_id)
    elif list_reply_id[1] == "d":
        payload = fcm_payload.build_pg_fcm_payload(wa_id)
    elif list_reply_id[1] == "e":
        payload = gmbs_payload.build_gmbs_payload(wa_id)
    elif list_reply_id[1] == "f":
        payload = pgd_payload.build_pgd_payload(wa_id)
    return _post_to_meta(payload)

def send_bXX_details(wa_id: str, button_reply_id: str):
    """Send the details for the first school option based on the button reply ID."""
    if button_reply_id[1] == "c":
        send_bcX_details(wa_id, button_reply_id)
    elif button_reply_id[1] == "d":
        send_bdX_details(wa_id, button_reply_id)      

def send_bXXX_details(wa_id: str, list_reply_id: str):
    """Send the details for the first branch option based on the list reply ID."""
    if list_reply_id[1] == "a":
        send_baXX_details(wa_id, list_reply_id)
    elif list_reply_id[1] == "b":
        send_bbXX_details(wa_id, list_reply_id) 
    elif list_reply_id[1] == "c":
        send_bcXX_details(wa_id, list_reply_id) 
    elif list_reply_id[1] == "d":
        send_bdXX_details(wa_id, list_reply_id)        
    elif list_reply_id[1] == "e":
        send_beXX_details(wa_id, list_reply_id)
    elif list_reply_id[1] == "f":
        send_bfXX_details(wa_id, list_reply_id)


def send_bXXXX_details(wa_id: str, button_reply_id: str):
    """Send the details for the first course option based on the button reply ID."""
    if button_reply_id[1] == "a":
        send_baXXX_details(wa_id, button_reply_id)
    elif button_reply_id[1] == "b":
        send_bbXXX_details(wa_id, button_reply_id) 
    elif button_reply_id[1] == "c":
        send_bcXXX_details(wa_id, button_reply_id)   
    elif button_reply_id[1] == "d":
        send_bdXXX_details(wa_id, button_reply_id)        
    elif button_reply_id[1] == "e":
        send_beXXX_details(wa_id, button_reply_id)
    elif button_reply_id[1] == "f":
        send_bfXXX_details(wa_id, button_reply_id)   
    
    

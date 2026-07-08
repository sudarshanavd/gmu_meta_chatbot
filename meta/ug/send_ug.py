from meta.client import _post_to_meta
from payload.ug import *    
from meta.ug.fet.send_fet import (send_aaX_details,
                                  send_aaXX_details,
                                  send_aaXXX_details,
                                  send_aabXX_details,
                                  send_aabX_details
)
from meta.ug.fcm.send_fcm import (send_abaX_details,
                                  send_abaXX_details,
                                  send_abX_details,
                                  send_abXX_details,
                                  send_abXXX_details
                                  )
from meta.ug.gmsl.send_gmsl import (send_acXX_details,
                                    send_acXXX_details
)
from meta.ug.fbas.send_fbas import (send_adX_details,
                                    send_adXX_details,
                                    send_adXXX_details
                                    )
from meta.ug.fcit.send_fcit import (send_aeX_details,
                                    send_aeXX_details,
                                    send_aeXXX_details
                                    )
from meta.ug.rp.send_rp import (send_afXX_details,
                                send_afXXX_details
                                )
from meta.ug.bv.send_bv import (send_agXX_details,
                                send_agXXX_details)

def send_aX_details(wa_id: str, list_reply_id: str):
    """Send the details for the first program option based on the list reply ID."""
    if list_reply_id[1] == "a":
        payload = fet_payload.build_engineering_faculty_payload(wa_id)
    elif list_reply_id[1] == "b":
        payload = fcm_payload.build_commerce_faculty_payload(wa_id)
    elif list_reply_id[1] == "c":
        payload = gmsl_payload.build_law_faculty_payload(wa_id)
    elif list_reply_id[1] == "d":
        payload = fbas_payload.build_science_faculty_payload(wa_id)
    elif list_reply_id[1] == "e":
        payload = fcit_payload.build_computing_faculty_payload(wa_id)
    elif list_reply_id[1] == "f":
        payload = rp_payload.build_research_programs_payload(wa_id)
    elif list_reply_id[1] == "g":
        payload = bv_payload.build_b_voc_payload(wa_id)
    return _post_to_meta(payload)

def send_aXX_details(wa_id: str, button_reply_id: str):
    """Send the details for the first school option based on the button reply ID."""
    if button_reply_id[1] == "a":
        send_aaX_details(wa_id, button_reply_id)
    elif button_reply_id[1] == "b":
        send_abX_details(wa_id, button_reply_id) 
    elif button_reply_id[1] == "d":
        send_adX_details(wa_id, button_reply_id)        
    elif button_reply_id[1] == "e":
        send_aeX_details(wa_id, button_reply_id)

def send_aXXX_details(wa_id: str, list_reply_id: str):
    """Send the details for the first branch option based on the list reply ID."""
    if list_reply_id[1] == "a":
        print("test aab")
        send_aaXX_details(wa_id, list_reply_id)
    elif list_reply_id[1] == "b":
        send_abXX_details(wa_id, list_reply_id) 
    elif list_reply_id[1] == "c":
        send_acXX_details(wa_id, list_reply_id) 
    elif list_reply_id[1] == "d":
        send_adXX_details(wa_id, list_reply_id)        
    elif list_reply_id[1] == "e":
        send_aeXX_details(wa_id, list_reply_id)
    elif list_reply_id[1] == "f":
        send_afXX_details(wa_id, list_reply_id)
    elif list_reply_id[1] == "g":
        send_agXX_details(wa_id, list_reply_id)

def send_aXXXX_details(wa_id: str, button_reply_id: str):
    """Send the details for the first course option based on the button reply ID."""
    if button_reply_id[1] == "a":
        send_aaXXX_details(wa_id, button_reply_id)
    elif button_reply_id[1] == "b":
        send_abXXX_details(wa_id, button_reply_id) 
    elif button_reply_id[1] == "c":
        send_acXXX_details(wa_id, button_reply_id)   
    elif button_reply_id[1] == "d":
        send_adXXX_details(wa_id, button_reply_id)        
    elif button_reply_id[1] == "e":
        send_aeX_details(wa_id, button_reply_id)
    elif button_reply_id[1] == "f":
        send_afXXX_details(wa_id, button_reply_id)   
    elif button_reply_id[1] == "g":
        send_agXXX_details(wa_id, button_reply_id)   

from meta.client import _post_to_meta
from payload.ug.fet import fet_payload 
from payload.ug.fbas import *
from meta.ug.fbas.sas.send_sas import (send_adcX_details,
                                       send_adcXX_details
                                       )
from meta.ug.fbas.scbs.send_scbs import (send_adbX_details,
                                         send_adbXX_details
                                         )
from meta.ug.fbas.smps.send_smps import (send_adaX_details,
                                         send_adaXX_details)

def send_adX_details(wa_id: str, button_reply_id: str):
    """Send the details for the first school option based on the button reply ID."""
    if button_reply_id[2] == "a":
        payload = smps_payload.build_school_of_mathematical_physical_sciences_payload(wa_id)
    elif button_reply_id[2] == "b":
        payload = scbs_payload.build_school_of_chemical_biological_sciences_payload(wa_id)
    elif button_reply_id[2] == "c":
        payload = sas_payload.build_school_of_applied_sciences_payload(wa_id)
    return _post_to_meta(payload)

def send_adXX_details(wa_id: str, button_reply_id: str):
    """Send the details for the first branch option based on the button reply ID."""
    if button_reply_id[2] == "a":
        send_adaX_details(wa_id, button_reply_id)
    elif button_reply_id[2] == "b":
        send_adbX_details(wa_id, button_reply_id)
    elif button_reply_id[2] == "c":
        send_adcX_details(wa_id, button_reply_id)

def send_adXXX_details(wa_id: str, button_reply_id: str):
    """Send the details for the first course option based on the button reply ID."""
    if button_reply_id[2] == "a":
        send_adaXX_details(wa_id, button_reply_id)
    elif button_reply_id[2] == "b":
        send_adbXX_details(wa_id, button_reply_id)
    elif button_reply_id[2] == "c":
        send_adcXX_details(wa_id, button_reply_id)

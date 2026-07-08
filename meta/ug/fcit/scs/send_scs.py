from meta.client import _post_to_meta
from payload.ug.fcit.scs.sub import bai_payoad,bcy_payoads,bds_payoad
from meta.ug.fcit.scs.sub import aida,cy,ds

def send_aebX_details(wa_id, button_reply_id):
    """Send the details for the first course option based on the button reply ID."""
    if button_reply_id[3] == "a":
        payload = bds_payoad.build_bca_ds_program_payload(wa_id)   
    elif button_reply_id[3] == "b":
        payload = bcy_payoads.build_bca_cy_program_payload(wa_id)   
    elif button_reply_id[3] == "b":
        payload = bai_payoad.build_bca_cy_branch_website_payload(wa_id)   
    
    return _post_to_meta(payload)

def send_aebXX_details(wa_id, button_reply_id):
    """Send the details for the first course option based on the button reply ID."""
    if button_reply_id[3] == "a":
        ds.send_aebaX_details(wa_id, button_reply_id)
    elif button_reply_id[3] == "b":
        cy.send_aebbX_details(wa_id, button_reply_id)
    elif button_reply_id[3] == "c":
        aida.send_aebcX_details(wa_id, button_reply_id)
    
   

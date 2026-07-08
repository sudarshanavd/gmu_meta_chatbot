from meta.client import _post_to_meta
from payload.pg.pgd.sub import pgdaf_payoad,pgdai_payoad,pgdes_payoad
from meta.ug.gmsl.sub import send_bbl,send_bcl,send_llb

def send_bfXX_details(wa_id, button_reply_id):
    """Send the details for the first course option based on the button reply ID."""
    if button_reply_id[3] == "a":
        payload = pgdai_payoad.build_pgd_ai_iot_program_payload(wa_id)
    elif button_reply_id[3] == "b":
        payload = pgdes_payoad.build_pgd_embedded_systems_program_payload(wa_id)   
    elif button_reply_id[3] == "c":
        payload = pgdaf_payoad.build_pgd_accounting_finance_program_payload(wa_id)
    
    return _post_to_meta(payload)

def send_bfXXX_details(wa_id, button_reply_id):
    if button_reply_id[3] == "a":
        send_llb.send_bbfaX_details(wa_id, button_reply_id)
    if button_reply_id[3] == "b":
        send_bbl.send_bfabX_details(wa_id, button_reply_id)
    if button_reply_id[3] == "c":
        send_bcl.send_bfacX_details(wa_id, button_reply_id)

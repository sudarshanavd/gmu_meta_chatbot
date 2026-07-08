from meta.client import _post_to_meta
from payload.ug.fet.scst.sub import cse_payoad

def send_aaaaX_details(wa_id: str, button_reply_id: str):
    if button_reply_id[4] == "a":
        payload = cse_payoad.build_cse_program_details_payload(wa_id)
    elif button_reply_id[4] == "b":
        payload = cse_payoad.build_cse_fee_duration_payload(wa_id)
    elif button_reply_id[4] == "c":
        payload = cse_payoad.build_cse_branch_website_payload(wa_id)    
    return _post_to_meta(payload)

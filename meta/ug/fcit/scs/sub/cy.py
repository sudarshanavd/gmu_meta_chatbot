from meta.client import _post_to_meta
from payload.ug.fcit.scs.sub import bcy_payoads

def send_aebbX_details(wa_id: str, button_reply_id: str):
    if button_reply_id[4] == "a":
        payload = bcy_payoads.build_bca_cy_program_details_payload(wa_id)
    elif button_reply_id[4] == "b":
        payload = bcy_payoads.build_bca_cy_fee_duration_payload(wa_id)
    elif button_reply_id[4] == "c":
        payload = bcy_payoads.build_bca_cy_branch_website_payload(wa_id)
    return _post_to_meta(payload)

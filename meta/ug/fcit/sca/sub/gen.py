from meta.client import _post_to_meta
from payload.ug.fcit.sca.sub import bca_payoad

def send_aeaaX_details(wa_id: str, button_reply_id: str):
    if button_reply_id[4] == "a":
        payload = bca_payoad.build_bca_general_program_details_payload(wa_id)
    elif button_reply_id[4] == "b":
        payload = bca_payoad.build_bca_general_fee_duration_payload(wa_id)
    elif button_reply_id[4] == "c":
        payload = bca_payoad.build_bca_general_branch_website_payload(wa_id)
    return _post_to_meta(payload)

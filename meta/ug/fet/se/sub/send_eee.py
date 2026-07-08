from meta.client import _post_to_meta
from payload.ug.fet.se.sub import eee_payoad

def send_aabbX_details(wa_id: str, button_reply_id: str):
    if button_reply_id[4] == "a":
        payload = eee_payoad.build_eee_program_details_payload(wa_id)
    elif button_reply_id[4] == "b":
        payload = eee_payoad.build_eee_fee_duration_payload(wa_id)
    elif button_reply_id[4] == "c":
        payload = eee_payoad.build_eee_branch_website_payload(wa_id)
    return _post_to_meta(payload)

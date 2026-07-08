from meta.client import _post_to_meta
from payload.ug.fcm.sc.sub import at_payoad

def send_abadX_details(wa_id: str, button_reply_id: str):
    if button_reply_id[4] == "a":
        payload = at_payoad.build_at_program_details_payload(wa_id)
    elif button_reply_id[4] == "b":
        payload = at_payoad.build_at_fee_duration_payload(wa_id)
    elif button_reply_id[4] == "c":
        payload = at_payoad.build_at_branch_website_payload(wa_id)
    return _post_to_meta(payload)

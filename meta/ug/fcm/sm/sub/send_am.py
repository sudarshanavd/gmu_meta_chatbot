from meta.client import _post_to_meta
from payload.ug.fcm.sm.sub import am_payload

def send_abbeX_details(wa_id: str, button_reply_id: str):
    if button_reply_id[4] == "a":
        payload = am_payload.build_am_program_details_payload(wa_id)
    elif button_reply_id[4] == "b":
        payload = am_payload.build_am_fee_duration_payload(wa_id)
    elif button_reply_id[4] == "c":
        payload = am_payload.build_am_branch_website_payload(wa_id)
    return _post_to_meta(payload)

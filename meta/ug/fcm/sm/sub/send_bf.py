from meta.client import _post_to_meta
from payload.ug.fcm.sm.sub import bf_payload

def send_abbbX_details(wa_id: str, button_reply_id: str):
    if button_reply_id[4] == "a":
        payload = bf_payload.build_bf_program_details_payload(wa_id)
    elif button_reply_id[4] == "b":
        payload = bf_payload.build_bf_fee_duration_payload(wa_id)
    elif button_reply_id[4] == "c":
        payload = bf_payload.build_bf_branch_website_payload(wa_id)
    return _post_to_meta(payload)

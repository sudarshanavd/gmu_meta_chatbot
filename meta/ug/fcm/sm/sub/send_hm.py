from meta.client import _post_to_meta
from payload.ug.fcm.sm.sub import hm_payload

def send_abbgX_details(wa_id: str, button_reply_id: str):
    if button_reply_id[4] == "a":
        payload = hm_payload.build_hm_program_details_payload(wa_id)
    elif button_reply_id[4] == "b":
        payload = hm_payload.build_hm_fee_duration_payload(wa_id)
    elif button_reply_id[4] == "c":
        payload = hm_payload.build_hm_branch_website_payload(wa_id)
    return _post_to_meta(payload)

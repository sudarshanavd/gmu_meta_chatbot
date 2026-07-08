from meta.client import _post_to_meta
from payload.ug.fcm.sm.sub import dm_payload

def send_abbdX_details(wa_id: str, button_reply_id: str):
    if button_reply_id[4] == "a":
        payload = dm_payload.build_dme_program_details_payload(wa_id)
    elif button_reply_id[4] == "b":
        payload = dm_payload.build_dme_fee_duration_payload(wa_id)
    elif button_reply_id[4] == "c":
        payload = dm_payload.build_dme_branch_website_payload(wa_id)
    return _post_to_meta(payload)

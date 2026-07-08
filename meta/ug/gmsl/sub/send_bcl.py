from meta.client import _post_to_meta
from payload.ug.gmsl.sub import bcl_payload
def send_acacX_details(wa_id: str, button_reply_id: str):
    if button_reply_id[4] == "a":
        payload = bcl_payload.build_bcomllb_program_details_payload(wa_id)
    elif button_reply_id[4] == "b":
        payload = bcl_payload.build_bcomllb_fee_duration_payload(wa_id)
    elif button_reply_id[4] == "c":
        payload = bcl_payload.build_bcomllb_branch_website_payload(wa_id)
    return _post_to_meta(payload)

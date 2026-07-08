from meta.client import _post_to_meta
from payload.ug.gmsl.sub import bbl_payload

def send_acabX_details(wa_id: str, button_reply_id: str):
    if button_reply_id[4] == "a":
        payload = bbl_payload.build_bballb_program_details_payload(wa_id)
    elif button_reply_id[4] == "b":
        payload = bbl_payload.build_bballb_fee_duration_payload(wa_id)
    elif button_reply_id[4] == "c":
        payload = bbl_payload.build_bballb_branch_website_payload(wa_id)
    return _post_to_meta(payload)


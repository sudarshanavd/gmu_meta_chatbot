from meta.client import _post_to_meta
from payload.ug.gmsl.sub import llb_payload
def send_acaaX_details(wa_id: str, button_reply_id: str):
    if button_reply_id[4] == "a":
        payload = llb_payload.build_llb_program_details_payload(wa_id)
    elif button_reply_id[4] == "b":
        payload = llb_payload.build_llb_fee_duration_payload(wa_id)
    elif button_reply_id[4] == "c":
        payload = llb_payload.build_llb_branch_website_payload(wa_id)
    return _post_to_meta(payload)

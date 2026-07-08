from meta.client import _post_to_meta
from payload.ug.fet.scst.sub import ise_payload

def send_aaabX_details(wa_id: str, button_reply_id: str):
    if button_reply_id[4] == "a":
        payload = ise_payload.build_ise_program_details_payload(wa_id)
    elif button_reply_id[4] == "b":
        payload = ise_payload.build_ise_fee_duration_payload(wa_id)
    elif button_reply_id[4] == "c":
        payload = ise_payload.build_ise_branch_website_payload(wa_id)    
    return _post_to_meta(payload)

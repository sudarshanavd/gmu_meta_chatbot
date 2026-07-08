from meta.client import _post_to_meta
from payload.ug.fet.se.sub import ed_payoad

def send_aabdX_details(wa_id: str, button_reply_id: str):
    if button_reply_id[4] == "a":
        payload = ed_payoad.build_ed_program_details_payload(wa_id)
    elif button_reply_id[4] == "b":
        payload = ed_payoad.build_ed_fee_duration_payload(wa_id)
    elif button_reply_id[4] == "c":
        payload = ed_payoad.build_ed_branch_website_payload(wa_id)
    return _post_to_meta(payload)

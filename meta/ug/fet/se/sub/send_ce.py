from meta.client import _post_to_meta
from payload.ug.fet.se.sub import ce_payoad

def send_aabeX_details(wa_id: str, button_reply_id: str):
    if button_reply_id[4] == "a":
        payload = ce_payoad.build_ce_program_details_payload(wa_id)
    elif button_reply_id[4] == "b":
        payload = ce_payoad.build_ce_fee_duration_payload(wa_id)
    elif button_reply_id[4] == "c":
        payload = ce_payoad.build_ce_branch_website_payload(wa_id)
    return _post_to_meta(payload)

from meta.client import _post_to_meta
from payload.ug.fet.se.sub import ece_payoad

def send_aabaX_details(wa_id: str, button_reply_id: str):
    if button_reply_id[4] == "a":
        payload = ece_payoad.build_ece_program_details_payload(wa_id)
    elif button_reply_id[4] == "b":
        payload = ece_payoad.build_ece_fee_duration_payload(wa_id)
    elif button_reply_id[4] == "c":
        payload = ece_payoad.build_ece_branch_website_payload(wa_id)
    return _post_to_meta(payload)

from meta.client import _post_to_meta
from payload.ug.fet.se.sub import me_payoad

def send_aabgX_details(wa_id: str, button_reply_id: str):
    if button_reply_id[4] == "a":
        payload = me_payoad.build_me_program_details_payload(wa_id)
    elif button_reply_id[4] == "b":
        payload = me_payoad.build_me_fee_duration_payload(wa_id)
    elif button_reply_id[4] == "c":
        payload = me_payoad.build_me_branch_website_payload(wa_id)
    return _post_to_meta(payload)

from meta.client import _post_to_meta
from payload.ug.fet.scst.sub import cc_payoad

def send_aaahX_details(wa_id: str, button_reply_id: str):
    if button_reply_id[4] == "a":
        payload = cc_payoad.build_cc_program_details_payload(wa_id)
    elif button_reply_id[4] == "b":
        payload = cc_payoad.build_cc_fee_duration_payload(wa_id)
    elif button_reply_id[4] == "c":
        payload = cc_payoad.build_cc_branch_website_payload(wa_id)
    return _post_to_meta(payload)

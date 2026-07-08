from meta.client import _post_to_meta
from payload.ug.fet.scst.sub import cy_payoad

def send_aaagX_details(wa_id: str, button_reply_id: str):
    if button_reply_id[4] == "a":
        payload = cy_payoad.build_cy_program_details_payload(wa_id)
    elif button_reply_id[4] == "b":
        payload = cy_payoad.build_cy_fee_duration_payload(wa_id)
    elif button_reply_id[4] == "c":
        payload = cy_payoad.build_cy_branch_website_payload(wa_id)
    return _post_to_meta(payload)

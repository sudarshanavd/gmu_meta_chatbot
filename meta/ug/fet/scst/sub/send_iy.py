from meta.client import _post_to_meta
from payload.ug.fet.scst.sub import iy_payoad

def send_aaaiX_details(wa_id: str, button_reply_id: str):
    if button_reply_id[4] == "a":
        payload = iy_payoad.build_iy_program_details_payload(wa_id)
    elif button_reply_id[4] == "b":
        payload = iy_payoad.build_iy_fee_duration_payload(wa_id)
    elif button_reply_id[4] == "c":
        payload = iy_payoad.build_iy_branch_website_payload(wa_id)
    return _post_to_meta(payload)

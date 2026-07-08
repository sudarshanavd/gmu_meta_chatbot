from meta.client import _post_to_meta
from payload.ug.bv.sub import bvevt_payoad

def send_agaaX_details(wa_id: str, button_reply_id: str):
    if button_reply_id[4] == "a":
        payload = bvevt_payoad.build_bvoc_evt_program_details_payload(wa_id)
    elif button_reply_id[4] == "b":
        payload = bvevt_payoad.build_bvoc_evt_fee_duration_payload(wa_id)
    elif button_reply_id[4] == "c":
        payload = bvevt_payoad.build_bvoc_evt_branch_website_payload(wa_id)
    return _post_to_meta(payload)


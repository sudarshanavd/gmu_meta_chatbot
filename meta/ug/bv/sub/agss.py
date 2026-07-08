from meta.client import _post_to_meta
from payload.ug.bv.sub import bvagss_payoad

def send_agadX_details(wa_id: str, button_reply_id: str):
    if button_reply_id[4] == "a":
        payload = bvagss_payoad.build_bvoc_agss_program_details_payload(wa_id)
    elif button_reply_id[4] == "b":
        payload = bvagss_payoad.build_bvoc_agss_fee_duration_payload(wa_id)
    elif button_reply_id[4] == "c":
        payload = bvagss_payoad.build_bvoc_agss_branch_website_payload(wa_id)
    return _post_to_meta(payload)


from meta.client import _post_to_meta
from payload.ug.bv.sub import bvfdam_payoad

def send_agabX_details(wa_id: str, button_reply_id: str):
    if button_reply_id[4] == "a":
        payload = bvfdam_payoad.build_bvoc_fdam_program_details_payload(wa_id)
    elif button_reply_id[4] == "b":
        payload = bvfdam_payoad.build_bvoc_fdam_fee_duration_payload(wa_id)
    elif button_reply_id[4] == "c":
        payload = bvfdam_payoad.build_bvoc_fdam_branch_website_payload(wa_id)
    return _post_to_meta(payload)


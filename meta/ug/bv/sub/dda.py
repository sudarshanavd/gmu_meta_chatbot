from meta.client import _post_to_meta
from payload.ug.bv.sub import bvdd_payoad

def send_agacX_details(wa_id: str, button_reply_id: str):
    if button_reply_id[4] == "a":
        payload = bvdd_payoad.build_bvoc_dda_program_details_payload(wa_id)
    elif button_reply_id[4] == "b":
        payload = bvdd_payoad.build_bvoc_dda_fee_duration_payload(wa_id)
    elif button_reply_id[4] == "c":
        payload = bvdd_payoad.build_bvoc_dda_branch_website_payload(wa_id)
    return _post_to_meta(payload)


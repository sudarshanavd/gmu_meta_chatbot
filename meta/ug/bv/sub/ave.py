from meta.client import _post_to_meta
from payload.ug.bv.sub import bvave_payoad

def send_agafX_details(wa_id: str, button_reply_id: str):
    if button_reply_id[4] == "a":
        payload = bvave_payoad.build_bsc_ave_program_details_payload(wa_id)
    elif button_reply_id[4] == "b":
        payload = bvave_payoad.build_bsc_ave_fee_duration_payload(wa_id)
    elif button_reply_id[4] == "c":
        payload = bvave_payoad.build_bsc_ave_branch_website_payload(wa_id)
    return _post_to_meta(payload)

  
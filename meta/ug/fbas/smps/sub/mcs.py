from meta.client import _post_to_meta
from payload.ug.fbas.smps.sub import mcs_payoad

def send_adabX_details(wa_id: str, button_reply_id: str):
    if button_reply_id[4] == "a":
        payload = mcs_payoad.build_bsc_mcs_program_details_payload(wa_id)
    elif button_reply_id[4] == "b":
        payload = mcs_payoad.build_bsc_mcs_fee_duration_payload(wa_id)
    elif button_reply_id[4] == "c":
        payload = mcs_payoad.build_bsc_mcs_branch_website_payload(wa_id)
    return _post_to_meta(payload)

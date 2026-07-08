from meta.client import _post_to_meta
from payload.ug.fbas.smps.sub import scs_payoad

def send_adacX_details(wa_id: str, button_reply_id: str):
    if button_reply_id[4] == "a":
        payload = scs_payoad.build_bsc_scs_program_details_payload(wa_id)
    elif button_reply_id[4] == "b":
        payload = scs_payoad.build_bsc_scs_fee_duration_payload(wa_id)
    elif button_reply_id[4] == "c":
        payload = scs_payoad.build_bsc_scs_branch_website_payload(wa_id)
    return _post_to_meta(payload)

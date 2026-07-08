from meta.client import _post_to_meta
from payload.ug.fbas.scbs.sub import ccs_payoad

def send_adbbX_details(wa_id: str, button_reply_id: str):
    if button_reply_id[4] == "a":
        payload = ccs_payoad.build_bsc_ccs_program_details_payload(wa_id)
    elif button_reply_id[4] == "b":
        payload = ccs_payoad.build_bsc_ccs_fee_duration_payload(wa_id)
    elif button_reply_id[4] == "c":
        payload = ccs_payoad.build_bsc_ccs_branch_website_payload(wa_id)
    return _post_to_meta(payload)

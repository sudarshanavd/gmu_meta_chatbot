from meta.client import _post_to_meta
from payload.ug.fbas.sas.sub import fst_payoad

def send_adcaX_details(wa_id: str, button_reply_id: str):
    if button_reply_id[4] == "a":
        payload = fst_payoad.build_bsc_fst_program_details_payload(wa_id)
    elif button_reply_id[4] == "b":
        payload = fst_payoad.build_bsc_fst_fee_duration_payload(wa_id)
    elif button_reply_id[4] == "c":
        payload = fst_payoad.build_bsc_fst_branch_website_payload(wa_id)
    return _post_to_meta(payload)

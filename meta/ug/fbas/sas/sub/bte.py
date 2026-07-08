from meta.client import _post_to_meta
from payload.ug.fbas.sas.sub import bte_payoad

def send_adcbX_details(wa_id: str, button_reply_id: str):
    if button_reply_id[4] == "a":
        payload = bte_payoad.build_bsc_bte_program_details_payload(wa_id)
    elif button_reply_id[4] == "b":
        payload = bte_payoad.build_bsc_bte_fee_duration_payload(wa_id)
    elif button_reply_id[4] == "c":
        payload = bte_payoad.build_bsc_bte_branch_website_payload(wa_id)
    return _post_to_meta(payload)

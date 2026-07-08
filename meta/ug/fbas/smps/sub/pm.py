from meta.client import _post_to_meta
from payload.ug.fbas.smps.sub import pm_payoad

def send_aabfX_details(wa_id: str, button_reply_id: str):
    if button_reply_id[4] == "a":
        payload = pm_payoad.build_bsc_pm_program_details_payload(wa_id)
    elif button_reply_id[4] == "b":
        payload = pm_payoad.build_bsc_pm_fee_duration_payload(wa_id)
    elif button_reply_id[4] == "c":
        payload = pm_payoad.build_bsc_pm_branch_website_payload(wa_id)
    return _post_to_meta(payload)

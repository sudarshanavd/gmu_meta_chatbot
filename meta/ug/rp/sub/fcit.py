from meta.client import _post_to_meta
from payload.ug.rp.sub import fcit_payoad

def send_afabX_details(wa_id: str, button_reply_id: str):
    if button_reply_id[4] == "a":
        payload = fcit_payoad.build_phd_fcit_program_details_payload(wa_id)
    elif button_reply_id[4] == "b":
        payload = fcit_payoad.build_phd_fcit_fee_duration_payload(wa_id)
    elif button_reply_id[4] == "c":
        payload = fcit_payoad.build_phd_fcit_branch_website_payload(wa_id)
    return _post_to_meta(payload)


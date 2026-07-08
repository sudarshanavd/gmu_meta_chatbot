from meta.client import _post_to_meta
from payload.ug.rp.sub import fcm_payoad

def send_afadX_details(wa_id: str, button_reply_id: str):
    if button_reply_id[4] == "a":
        payload = fcm_payoad.build_phd_fcm_program_details_payload(wa_id)
    elif button_reply_id[4] == "b":
        payload = fcm_payoad.build_phd_fcm_fee_duration_payload(wa_id)
    elif button_reply_id[4] == "c":
        payload = fcm_payoad.build_phd_fcm_branch_website_payload(wa_id)
    return _post_to_meta(payload)


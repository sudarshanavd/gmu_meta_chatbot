from meta.client import _post_to_meta
from payload.ug.fcm.sc.sub import dabi_payoad

def send_ababX_details(wa_id: str, button_reply_id: str):
    if button_reply_id[4] == "a":
        payload = dabi_payoad.build_dabi_program_details_payload(wa_id)
    elif button_reply_id[4] == "b":
        payload = dabi_payoad.build_dabi_fee_duration_payload(wa_id)
    elif button_reply_id[4] == "c":
        payload = dabi_payoad.build_dabi_branch_website_payload(wa_id)
    return _post_to_meta(payload)

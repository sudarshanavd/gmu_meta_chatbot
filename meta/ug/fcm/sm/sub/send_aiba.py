from meta.client import _post_to_meta
from payload.ug.fcm.sm.sub import aba_payload

def send_abbcX_details(wa_id: str, button_reply_id: str):
    if button_reply_id[4] == "a":
        payload = aba_payload.build_aba_program_details_payload(wa_id)
    elif button_reply_id[4] == "b":
        payload = aba_payload.build_aba_fee_duration_payload(wa_id)
    elif button_reply_id[4] == "c":
        payload = aba_payload.build_aba_branch_website_payload(wa_id)
    return _post_to_meta(payload)

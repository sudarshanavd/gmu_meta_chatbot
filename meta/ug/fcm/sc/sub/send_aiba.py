from meta.client import _post_to_meta
from payload.ug.fcm.sc.sub import aba_payoad

def send_abacX_details(wa_id: str, button_reply_id: str):
    if button_reply_id[4] == "a":
        payload = aba_payoad.build_aba_program_details_payload(wa_id)
    elif button_reply_id[4] == "b":
        payload = aba_payoad.build_aba_fee_duration_payload(wa_id)
    elif button_reply_id[4] == "c":
        payload = aba_payoad.build_aba_branch_website_payload(wa_id)
    return _post_to_meta(payload)

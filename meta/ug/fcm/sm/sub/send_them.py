from meta.client import _post_to_meta
from payload.ug.fcm.sm.sub import them_payload

def send_abbfX_details(wa_id: str, button_reply_id: str):
    if button_reply_id[4] == "a":
        payload = them_payload.build_them_program_details_payload(wa_id)
    elif button_reply_id[4] == "b":
        payload = them_payload.build_them_fee_duration_payload(wa_id)
    elif button_reply_id[4] == "c":
        payload = them_payload.build_them_fee_duration_payload(wa_id)
    return _post_to_meta(payload)

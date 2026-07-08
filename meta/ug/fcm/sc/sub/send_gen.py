from meta.client import _post_to_meta
from payload.ug.fcm.sc.sub import gen_payload

def send_abaaX_details(wa_id: str, button_reply_id: str):
    if button_reply_id[4] == "a":
        payload = gen_payload.build_bcom_general_program_details_payload(wa_id)
    elif button_reply_id[4] == "b":
        payload = gen_payload.build_bcom_general_fee_duration_payload(wa_id)
    elif button_reply_id[4] == "c":
        payload =gen_payload.build_bcom_general_branch_website_payload(wa_id)
    return _post_to_meta(payload)

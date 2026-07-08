from meta.client import _post_to_meta
from payload.ug.fbas.scbs.sub import ces_payoad

def send_adbeX_details(wa_id: str, button_reply_id: str):
    if button_reply_id[4] == "a":
        payload = ces_payoad.build_bsc_ces_program_details_payload(wa_id)
    elif button_reply_id[4] == "b":
        payload = ces_payoad.build_bsc_ces_fee_duration_payload(wa_id)
    elif button_reply_id[4] == "c":
        payload = ces_payoad.build_bsc_ces_program_payload(wa_id)
    return _post_to_meta(payload)

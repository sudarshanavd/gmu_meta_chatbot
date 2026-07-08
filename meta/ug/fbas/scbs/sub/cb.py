from meta.client import _post_to_meta
from payload.ug.fbas.scbs.sub import cb_payoad

def send_adbdX_details(wa_id: str, button_reply_id: str):
    if button_reply_id[4] == "a":
        payload = cb_payoad.build_bsc_cb_program_details_payload(wa_id)
    elif button_reply_id[4] == "b":
        payload = cb_payoad.build_bsc_cb_fee_duration_payload(wa_id)
    elif button_reply_id[4] == "c":
        payload = cb_payoad.build_bsc_cb_branch_website_payload(wa_id)
    return _post_to_meta(payload)

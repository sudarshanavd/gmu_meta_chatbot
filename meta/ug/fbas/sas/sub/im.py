from meta.client import _post_to_meta
from payload.ug.fbas.sas.sub import im_payoad

def send_adccX_details(wa_id: str, button_reply_id: str):
    if button_reply_id[4] == "a":
        payload = im_payoad.build_bsc_im_program_details_payload(wa_id)
    elif button_reply_id[4] == "b":
        payload = im_payoad.build_bsc_im_fee_duration_payload(wa_id)
    elif button_reply_id[4] == "c":
        payload = im_payoad.build_bsc_im_branch_website_payload(wa_id)
    return _post_to_meta(payload)

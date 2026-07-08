from meta.client import _post_to_meta
from payload.ug.fet.scst.sub import ds_payoad

def send_aaafX_details(wa_id: str, button_reply_id: str):
    if button_reply_id[4] == "a":
        payload = ds_payoad.build_ds_program_details_payload(wa_id)
    elif button_reply_id[4] == "b":
        payload = ds_payoad.build_ds_fee_duration_payload(wa_id)
    elif button_reply_id[4] == "c":
        payload = ds_payoad.build_ds_branch_website_payload(wa_id)
    return _post_to_meta(payload)

from meta.client import _post_to_meta
from payload.ug.fcit.scs.sub import bds_payoad

def send_aebaX_details(wa_id: str, button_reply_id: str):
    if button_reply_id[4] == "a":
        payload = bds_payoad.build_bca_ds_program_details_payload(wa_id)
    elif button_reply_id[4] == "b":
        payload = bds_payoad.build_bca_ds_fee_duration_payload(wa_id)
    elif button_reply_id[4] == "c":
        payload = bds_payoad.build_bca_ds_branch_website_payload(wa_id)
    return _post_to_meta(payload)

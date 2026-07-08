from meta.client import _post_to_meta
from payload.pg.fcm.sc.sub import mfae_payoad

def send_bdabX_details(wa_id: str, button_reply_id: str):
    if button_reply_id[4] == "a":
        payload = mfae_payoad.build_mcom_fae_program_details_payload(wa_id)
    elif button_reply_id[4] == "b":
        payload = mfae_payoad.build_mcom_fae_fee_duration_payload(wa_id)
    elif button_reply_id[4] == "c":
        payload = mfae_payoad.build_mcom_fae_branch_website_payload(wa_id)
    return _post_to_meta(payload)

  
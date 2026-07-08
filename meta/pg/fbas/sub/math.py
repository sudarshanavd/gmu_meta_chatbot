from meta.client import _post_to_meta
from payload.pg.fbas.sub import mscm_payoad

def send_bbacX_details(wa_id: str, button_reply_id: str):
    if button_reply_id[4] == "a":
        payload = mscm_payoad.build_msc_mathematics_program_details_payload(wa_id)
    elif button_reply_id[4] == "b":
        payload = mscm_payoad.build_msc_mathematics_fee_duration_payload(wa_id)
    elif button_reply_id[4] == "c":
        payload = mscm_payoad.build_msc_mathematics_branch_website_payload(wa_id)
    return _post_to_meta(payload)

  
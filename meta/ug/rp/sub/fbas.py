from meta.client import _post_to_meta
from payload.ug.rp.sub import fbas_payoad

def send_afacX_details(wa_id: str, button_reply_id: str):
    if button_reply_id[4] == "a":
        payload = fbas_payoad.build_phd_fcit_program_details_payload(wa_id)
    elif button_reply_id[4] == "b":
        payload = fbas_payoad.build_phd_fcit_fee_duration_payload(wa_id)
    elif button_reply_id[4] == "c":
        payload = fbas_payoad.build_phd_fcit_branch_website_payload(wa_id)
    return _post_to_meta(payload)


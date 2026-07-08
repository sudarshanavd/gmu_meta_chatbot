from meta.client import _post_to_meta
from payload.ug.rp.sub import fet_payoad

def send_afaaX_details(wa_id: str, button_reply_id: str):
    if button_reply_id[4] == "a":
        payload = fet_payoad.build_phd_fet_program_details_payload(wa_id)
    elif button_reply_id[4] == "b":
        payload = fet_payoad.build_phd_fet_fee_duration_payload(wa_id)
    elif button_reply_id[4] == "c":
        payload = fet_payoad.build_phd_fet_branch_website_payload(wa_id)
    return _post_to_meta(payload)


from meta.client import _post_to_meta
from payload.pg.gmbs.sub import mbap_payoad

def send_beabX_details(wa_id: str, button_reply_id: str):
    if button_reply_id[4] == "a":
        payload = mbap_payoad.build_mba_professional_program_details_payload(wa_id)
    elif button_reply_id[4] == "b":
        payload = mbap_payoad.build_mba_professional_fee_duration_payload(wa_id)
    elif button_reply_id[4] == "c":
        payload = mbap_payoad.build_mba_professional_branch_website_payload(wa_id)
    return _post_to_meta(payload)
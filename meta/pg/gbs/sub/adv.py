from meta.client import _post_to_meta
from payload.pg.gmbs.sub import mbaa_payoad

def send_beacX_details(wa_id: str, button_reply_id: str):
    if button_reply_id[4] == "a":
        payload = mbaa_payoad.build_mba_advanced_program_details_payload(wa_id)
    elif button_reply_id[4] == "b":
        payload = mbaa_payoad.build_mba_advanced_fee_duration_payload(wa_id)
    elif button_reply_id[4] == "c":
        payload = mbaa_payoad.build_mba_advanced_branch_website_payload(wa_id)
    return _post_to_meta(payload)
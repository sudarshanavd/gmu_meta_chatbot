from meta.client import _post_to_meta
from payload.pg.gmbs.sub import mbai_payoad

def send_beadX_details(wa_id: str, button_reply_id: str):
    if button_reply_id[4] == "a":
        payload = mbai_payoad.build_mba_international_program_details_payload(wa_id)
    elif button_reply_id[4] == "b":
        payload = mbai_payoad.build_mba_international_fee_duration_payload(wa_id)
    elif button_reply_id[4] == "c":
        payload = mbai_payoad.build_mba_international_branch_website_payload(wa_id)
    return _post_to_meta(payload)
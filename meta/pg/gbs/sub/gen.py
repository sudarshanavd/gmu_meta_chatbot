from meta.client import _post_to_meta
from payload.pg.gmbs.sub import mbag_payoad

def send_beaaX_details(wa_id: str, button_reply_id: str):
    if button_reply_id[4] == "a":
        payload = mbag_payoad.build_mba_program_details_payload(wa_id)
    elif button_reply_id[4] == "b":
        payload = mbag_payoad.build_mba_fee_duration_payload(wa_id)
    elif button_reply_id[4] == "c":
        payload = mbag_payoad.build_mba_branch_website_payload(wa_id)
    return _post_to_meta(payload)

  
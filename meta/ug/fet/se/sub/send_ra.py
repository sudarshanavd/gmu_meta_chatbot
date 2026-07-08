from meta.client import _post_to_meta
from payload.ug.fet.se.sub import ra_payoad

def send_aabcX_details(wa_id: str, button_reply_id: str):
    if button_reply_id[4] == "a":
        payload = ra_payoad.build_ra_program_details_payload(wa_id)
    elif button_reply_id[4] == "b":
        payload = ra_payoad.build_ra_fee_duration_payload(wa_id)
    elif button_reply_id[4] == "c":
        payload = ra_payoad.build_ra_branch_website_payload(wa_id)
    return _post_to_meta(payload)

from meta.client import _post_to_meta
from payload.ug.fbas.scbs.sub import cz_payoad

def send_adbcX_details(wa_id: str, button_reply_id: str):
    if button_reply_id[4] == "a":
        payload = cz_payoad.build_bsc_cz_program_details_payload(wa_id)
    elif button_reply_id[4] == "b":
        payload = cz_payoad.build_bsc_cz_fee_duration_payload(wa_id)
    elif button_reply_id[4] == "c":
        payload = cz_payoad.build_bsc_cz_branch_website_payload(wa_id)
    return _post_to_meta(payload)

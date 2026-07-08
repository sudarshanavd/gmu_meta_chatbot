from meta.client import _post_to_meta
from payload.pg.gmsas.sub import gsbgt_payoad

def send_baagX_details(wa_id: str, button_reply_id: str):
    if button_reply_id[4] == "a":
        payload = gsbgt_payoad.build_mtech_bgt_program_details_payload(wa_id)
    elif button_reply_id[4] == "b":
        payload = gsbgt_payoad.build_mtech_bgt_fee_duration_payload(wa_id)
    elif button_reply_id[4] == "c":
        payload = gsbgt_payoad.build_mtech_bgt_branch_website_payload(wa_id)
    return _post_to_meta(payload)

  
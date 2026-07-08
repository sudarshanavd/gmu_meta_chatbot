from meta.client import _post_to_meta
from payload.pg.gmsas.sub import gssess_payoad

def send_baaeX_details(wa_id: str, button_reply_id: str):
    if button_reply_id[4] == "a":
        payload = gssess_payoad.build_mtech_sesse_program_details_payload(wa_id)
    elif button_reply_id[4] == "b":
        payload = gssess_payoad.build_mtech_sesse_fee_duration_payload(wa_id)
    elif button_reply_id[4] == "c":
        payload = gssess_payoad.build_mtech_sesse_branch_website_payload(wa_id)
    return _post_to_meta(payload)

  
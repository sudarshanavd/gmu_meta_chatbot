from meta.client import _post_to_meta
from payload.pg.gmsas.sub import gssga_payoad

def send_baaiX_details(wa_id: str, button_reply_id: str):
    if button_reply_id[4] == "a":
        payload = gssga_payoad.build_mtech_sga_program_details_payload(wa_id)
    elif button_reply_id[4] == "b":
        payload = gssga_payoad.build_mtech_sga_fee_duration_payload(wa_id)
    elif button_reply_id[4] == "c":
        payload = gssga_payoad.build_mtech_sga_branch_website_payload(wa_id)
    return _post_to_meta(payload)
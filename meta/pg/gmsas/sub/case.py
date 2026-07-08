from meta.client import _post_to_meta
from payload.pg.gmsas.sub import gsca_payoad

def send_baadX_details(wa_id: str, button_reply_id: str):
    if button_reply_id[4] == "a":
        payload = gsca_payoad.build_mtech_case_program_details_payload(wa_id)
    elif button_reply_id[4] == "b":
        payload = gsca_payoad.build_mtech_case_fee_duration_payload(wa_id)
    elif button_reply_id[4] == "c":
        payload = gsca_payoad.build_mtech_case_branch_website_payload(wa_id)
    return _post_to_meta(payload)

  
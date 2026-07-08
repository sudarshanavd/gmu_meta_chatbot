from meta.client import _post_to_meta
from payload.pg.gmsas.sub import gspdm_payoad

def send_baahX_details(wa_id: str, button_reply_id: str):
    if button_reply_id[4] == "a":
        payload = gspdm_payoad.build_mtech_pdm_program_details_payload(wa_id)
    elif button_reply_id[4] == "b":
        payload = gspdm_payoad.build_mtech_pdm_fee_duration_payload(wa_id)
    elif button_reply_id[4] == "c":
        payload = gspdm_payoad.build_mtech_pdm_branch_website_payload(wa_id)
    return _post_to_meta(payload)
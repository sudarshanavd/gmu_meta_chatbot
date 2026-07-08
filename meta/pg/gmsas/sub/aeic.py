from meta.client import _post_to_meta
from payload.pg.gmsas.sub import gsaeic_payoad

def send_baafX_details(wa_id: str, button_reply_id: str):
    if button_reply_id[4] == "a":
        payload = gsaeic_payoad.build_mtech_aeics_program_details_payload(wa_id)
    elif button_reply_id[4] == "b":
        payload = gsaeic_payoad.build_mtech_aeics_fee_duration_payload(wa_id)
    elif button_reply_id[4] == "c":
        payload = gsaeic_payoad.build_mtech_aeics_branch_website_payload(wa_id)
    return _post_to_meta(payload)

  
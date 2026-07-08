from meta.client import _post_to_meta
from payload.pg.gmsas.sub import gsde_payoad

def send_baacX_details(wa_id: str, button_reply_id: str):
    if button_reply_id[4] == "a":
        payload = gsde_payoad.build_mtech_de_program_details_payload(wa_id)
    elif button_reply_id[4] == "b":
        payload = gsde_payoad.build_mtech_de_fee_duration_payload(wa_id)
    elif button_reply_id[4] == "c":
        payload = gsde_payoad.build_mtech_de_branch_website_payload(wa_id)
    return _post_to_meta(payload)

  
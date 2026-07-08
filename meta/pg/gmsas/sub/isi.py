from meta.client import _post_to_meta
from payload.pg.gmsas.sub import gsisi_payoad

def send_baajX_details(wa_id: str, button_reply_id: str):
    if button_reply_id[4] == "a":
        payload = gsisi_payoad.build_mtech_isiiot_program_details_payload(wa_id)
    elif button_reply_id[4] == "b":
        payload = gsisi_payoad.build_mtech_isiiot_fee_duration_payload(wa_id)
    elif button_reply_id[4] == "c":
        payload = gsisi_payoad.build_mtech_isiiot_branch_website_payload(wa_id)
    return _post_to_meta(payload)
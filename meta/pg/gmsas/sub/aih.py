from meta.client import _post_to_meta
from payload.pg.gmsas.sub import gsai_payoad

def send_baabX_details(wa_id: str, button_reply_id: str):
    if button_reply_id[4] == "a":
        payload = gsai_payoad.build_mtech_aih_program_details_payload(wa_id)
    elif button_reply_id[4] == "b":
        payload = gsai_payoad.build_mtech_aih_fee_duration_payload(wa_id)
    elif button_reply_id[4] == "c":
        payload = gsai_payoad.build_mtech_aih_branch_website_payload(wa_id)
    return _post_to_meta(payload)

  
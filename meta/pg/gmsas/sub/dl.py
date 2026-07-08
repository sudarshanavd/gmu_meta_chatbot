from meta.client import _post_to_meta
from payload.pg.gmsas.sub import gsdl_payoad

def send_baaaX_details(wa_id: str, button_reply_id: str):
    if button_reply_id[4] == "a":
        payload = gsdl_payoad.build_mtech_deep_learning_program_details_payload(wa_id)
    elif button_reply_id[4] == "b":
        payload = gsdl_payoad.build_mtech_deep_learning_fee_duration_payload(wa_id)
    elif button_reply_id[4] == "c":
        payload = gsdl_payoad.build_mtech_deep_learning_branch_website_payload(wa_id)
    return _post_to_meta(payload)

  
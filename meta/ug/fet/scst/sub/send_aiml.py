from meta.client import _post_to_meta
from payload.ug.fet.scst.sub import aiml_payoad

def send_aaacX_details(wa_id: str, button_reply_id: str):
    if button_reply_id[4] == "a":
        payload = aiml_payoad.build_aiml_program_details_payload(wa_id)
    elif button_reply_id[4] == "b":
        payload = aiml_payoad.build_aiml_fee_duration_payload(wa_id)
    elif button_reply_id[4] == "c":
        payload = aiml_payoad.build_aiml_branch_website_payload(wa_id)
    return _post_to_meta(payload)

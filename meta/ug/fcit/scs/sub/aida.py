from meta.client import _post_to_meta
from payload.ug.fcit.scs.sub import bai_payoad

def send_aebcX_details(wa_id: str, button_reply_id: str):
    if button_reply_id[4] == "a":
        payload = bai_payoad.build_bca_ai_data_analytics_program_details_payload(wa_id)
    elif button_reply_id[4] == "b":
        payload = bai_payoad.build_bca_ai_data_analytics_fee_duration_payload(wa_id)
    elif button_reply_id[4] == "c":
        payload = bai_payoad.build_bca_cy_branch_website_payload(wa_id)
    return _post_to_meta(payload)

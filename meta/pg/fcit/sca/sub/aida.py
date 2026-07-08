from meta.client import _post_to_meta
from payload.pg.fcit.sca.sub import mcaai_payoad

def send_bcadX_details(wa_id: str, button_reply_id: str):
    if button_reply_id[4] == "a":
        payload = mcaai_payoad.build_mca_ai_data_analytics_program_details_payload(wa_id)
    elif button_reply_id[4] == "b":
        payload = mcaai_payoad.build_mca_ai_data_analytics_fee_duration_payload(wa_id)
    elif button_reply_id[4] == "c":
        payload = mcaai_payoad.build_mca_ai_data_analytics_branch_website_payload(wa_id)
    return _post_to_meta(payload)

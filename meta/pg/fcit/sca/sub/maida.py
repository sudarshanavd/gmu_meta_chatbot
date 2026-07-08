from meta.client import _post_to_meta
from payload.pg.fcit.sca.sub import mscai_payoad

def send_bcafX_details(wa_id: str, button_reply_id: str):
    if button_reply_id[4] == "a":
        payload = mscai_payoad.build_msc_ai_data_analytics_program_details_payload(wa_id)
    elif button_reply_id[4] == "b":
        payload = mscai_payoad.build_msc_ai_data_analytics_fee_duration_payload(wa_id)
    elif button_reply_id[4] == "c":
        payload = mscai_payoad.build_msc_ai_data_analytics_branch_website_payload(wa_id)
    return _post_to_meta(payload)

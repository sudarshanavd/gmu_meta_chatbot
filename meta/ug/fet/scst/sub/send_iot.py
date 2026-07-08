from meta.client import _post_to_meta
from payload.ug.fet.scst.sub import iot_payoad

def send_aaaeX_details(wa_id: str, button_reply_id: str):
    if button_reply_id[4] == "a":
        payload = iot_payoad.build_iot_program_details_payload(wa_id)
    elif button_reply_id[4] == "b":
        payload = iot_payoad.build_iot_fee_duration_payload(wa_id)
    elif button_reply_id[4] == "c":
        payload = iot_payoad.build_iot_branch_website_payload(wa_id)
    return _post_to_meta(payload)

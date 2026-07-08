from meta.client import _post_to_meta
from payload.pg.gmsas.sub import gsstcd_payoad

def send_baakX_details(wa_id: str, button_reply_id: str):
    if button_reply_id[4] == "a":
        payload = gsstcd_payoad.build_mtech_stcd_program_details_payload(wa_id)
    elif button_reply_id[4] == "b":
        payload = gsstcd_payoad.build_mtech_stcd_fee_duration_payload(wa_id)
    elif button_reply_id[4] == "c":
        payload = gsstcd_payoad.build_mtech_stcd_branch_website_payload(wa_id)
    return _post_to_meta(payload)
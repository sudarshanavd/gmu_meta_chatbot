from meta.client import _post_to_meta
from payload.ug.fet.se.sub import bt_payoad

def send_aabfX_details(wa_id: str, button_reply_id: str):
    if button_reply_id[4] == "a":
        payload = bt_payoad.build_bt_branch_website_payload(wa_id)
    elif button_reply_id[4] == "b":
        payload = bt_payoad.build_bt_fee_duration_payload(wa_id)
    elif button_reply_id[4] == "c":
        payload = bt_payoad.build_bt_branch_website_payload(wa_id)
    return _post_to_meta(payload)

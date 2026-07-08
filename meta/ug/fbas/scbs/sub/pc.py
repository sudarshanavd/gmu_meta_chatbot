from meta.client import _post_to_meta
from payload.ug.fbas.scbs.sub import pc_payoad

def send_adbaX_details(wa_id: str, button_reply_id: str):
    if button_reply_id[4] == "a":
        payload = pc_payoad.build_bsc_pc_program_details_payload(wa_id)
    elif button_reply_id[4] == "b":
        payload = pc_payoad.build_bsc_pc_fee_duration_payload(wa_id)
    elif button_reply_id[4] == "c":
        payload = pc_payoad.build_bsc_pc_branch_website_payload(wa_id)
    return _post_to_meta(payload)

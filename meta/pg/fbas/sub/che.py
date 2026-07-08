from meta.client import _post_to_meta
from payload.pg.fbas.sub import mscc_payoad

def send_bbabX_details(wa_id: str, button_reply_id: str):
    if button_reply_id[4] == "a":
        payload = mscc_payoad.build_msc_chemistry_program_details_payload(wa_id)
    elif button_reply_id[4] == "b":
        payload = mscc_payoad.build_msc_chemistry_branch_website_payload(wa_id)
    elif button_reply_id[4] == "c":
        payload = mscc_payoad.build_msc_chemistry_branch_website_payload(wa_id)
    return _post_to_meta(payload)

  
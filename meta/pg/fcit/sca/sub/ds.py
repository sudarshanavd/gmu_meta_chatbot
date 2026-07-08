from meta.client import _post_to_meta
from payload.pg.fcit.sca.sub import mcads_payoad

def send_bcabX_details(wa_id: str, button_reply_id: str):
    if button_reply_id[4] == "a":
        payload = mcads_payoad.build_mca_data_science_program_details_payload(wa_id)
    elif button_reply_id[4] == "b":
        payload = mcads_payoad.build_mca_data_science_fee_duration_payload(wa_id)
    elif button_reply_id[4] == "c":
        payload = mcads_payoad.build_mca_data_science_branch_website_payload(wa_id)
    return _post_to_meta(payload)

  
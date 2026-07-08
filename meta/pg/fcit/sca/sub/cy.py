from meta.client import _post_to_meta
from payload.pg.fcit.sca.sub import mcacy_payoad

def send_bcacX_details(wa_id: str, button_reply_id: str):
    if button_reply_id[4] == "a":
        payload = mcacy_payoad.build_mca_cyber_security_program_details_payload(wa_id)
    elif button_reply_id[4] == "b":
        payload = mcacy_payoad.build_mca_cyber_security_fee_duration_payload(wa_id)
    elif button_reply_id[4] == "c":
        payload = mcacy_payoad.build_mca_cyber_security_branch_website_payload(wa_id)
    return _post_to_meta(payload)

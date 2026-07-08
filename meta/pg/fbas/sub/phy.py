from meta.client import _post_to_meta
from payload.pg.fbas.sub import mscp_payoad

def send_bbaaX_details(wa_id: str, button_reply_id: str):
    if button_reply_id[4] == "a":
        payload = mscp_payoad.build_msc_physics_program_details_payload(wa_id)
    elif button_reply_id[4] == "b":
        payload = mscp_payoad.build_msc_physics_fee_duration_payload(wa_id)
    elif button_reply_id[4] == "c":
        payload = mscp_payoad.build_msc_physics_branch_website_payload(wa_id)
    return _post_to_meta(payload)

  
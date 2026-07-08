from meta.client import _post_to_meta
from payload.pg.fbas.sub import mscft_payoad

def send_bbadX_details(wa_id: str, button_reply_id: str):
    if button_reply_id[4] == "a":
        payload = mscft_payoad.build_msc_food_technology_program_details_payload(wa_id)
    elif button_reply_id[4] == "b":
        payload = mscft_payoad.build_msc_food_technology_fee_duration_payload(wa_id)
    elif button_reply_id[4] == "c":
        payload = mscft_payoad.build_msc_food_technology_branch_website_payload(wa_id)
    return _post_to_meta(payload)

  
from meta.client import _post_to_meta
from payload.pg.fcit.sca.sub import mscds_payoad

def send_bcaeX_details(wa_id: str, button_reply_id: str):
    if button_reply_id[4] == "a":
        payload = mscds_payoad.build_msc_data_science_program_details_payload(wa_id)
    elif button_reply_id[4] == "b":
        payload = mscds_payoad.build_msc_data_science_fee_duration_payload(wa_id)
    elif button_reply_id[4] == "c":
        payload = mscds_payoad.build_msc_data_science_branch_website_payload(wa_id)
    return _post_to_meta(payload)

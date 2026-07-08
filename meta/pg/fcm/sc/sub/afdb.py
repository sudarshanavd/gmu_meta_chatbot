from meta.client import _post_to_meta
from payload.pg.fcm.sc.sub import mafdb_payoad

def send_bdaaX_details(wa_id: str, button_reply_id: str):
    if button_reply_id[4] == "a":
        payload = mafdb_payoad.build_mcom_afdb_program_details_payload(wa_id)
    elif button_reply_id[4] == "b":
        payload = mafdb_payoad.build_mcom_afdb_fee_duration_payload(wa_id)
    elif button_reply_id[4] == "c":
        payload = mafdb_payoad.build_mcom_afdb_branch_website_payload(wa_id)
    return _post_to_meta(payload)

  
from meta.client import _post_to_meta
from payload.pg.pgd.sub import pgdai_payoad

def send_bfaaX_details(wa_id: str, button_reply_id: str):
    if button_reply_id[4] == "a":
        payload = pgdai_payoad.build_pgd_ai_iot_program_details_payload(wa_id)
    elif button_reply_id[4] == "b":
        payload = pgdai_payoad.build_pgd_ai_iot_fee_duration_payload(wa_id)
    elif button_reply_id[4] == "c":
        payload = pgdai_payoad.build_pgd_ai_iot_more_info_payload(wa_id)
    return _post_to_meta(payload)
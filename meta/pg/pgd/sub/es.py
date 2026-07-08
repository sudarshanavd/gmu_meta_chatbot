from meta.client import _post_to_meta
from payload.pg.pgd.sub import pgdes_payoad

def send_bfabX_details(wa_id: str, button_reply_id: str):
    if button_reply_id[4] == "a":
        payload = pgdes_payoad.build_pgd_embedded_systems_program_details_payload(wa_id)
    elif button_reply_id[4] == "b":
        payload = pgdes_payoad.build_pgd_embedded_systems_fee_duration_payload(wa_id)
    elif button_reply_id[4] == "c":
        payload = pgdes_payoad.build_pgd_embedded_systems_more_info_payload(wa_id)
    return _post_to_meta(payload)
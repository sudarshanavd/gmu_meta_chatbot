from meta.client import _post_to_meta
from payload.pg.pgd.sub import pgdaf_payoad

def send_bfacX_details(wa_id: str, button_reply_id: str):
    if button_reply_id[4] == "a":
        payload = pgdaf_payoad.build_pgd_accounting_finance_program_details_payload(wa_id)
    elif button_reply_id[4] == "b":
        payload = pgdaf_payoad.build_pgd_accounting_finance_fee_duration_payload(wa_id)
    elif button_reply_id[4] == "c":
        payload = pgdaf_payoad.build_pgd_accounting_finance_more_info_payload(wa_id)
    return _post_to_meta(payload)
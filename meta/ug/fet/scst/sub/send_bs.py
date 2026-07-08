from meta.client import _post_to_meta
from payload.ug.fet.scst.sub import ai_bbs_payoad

def send_aaadX_details(wa_id: str, button_reply_id: str):
    if button_reply_id[4] == "a":
        payload = ai_bbs_payoad.build_cs_aibcbs_program_details_payload(wa_id)
    elif button_reply_id[4] == "b":
        payload = ai_bbs_payoad.build_cs_aibcbs_fee_duration_payload(wa_id)
    elif button_reply_id[4] == "c":
        payload = ai_bbs_payoad.build_cs_aibcbs_branch_website_payload(wa_id)
    return _post_to_meta(payload)

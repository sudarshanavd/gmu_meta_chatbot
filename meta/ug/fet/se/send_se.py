from meta.client import _post_to_meta
from meta.ug.fet.se.sub import (send_bt,
                                send_ce,
                                send_ece,
                                send_ed,
                                send_eee,
                                send_me,
                                send_ra)

def send_aabX_details(wa_id, button_reply_id):
    """Send the details for the first course option based on the button reply ID."""
    if button_reply_id[3] == "a":
        from payload.ug.fet.se.sub import ece_payoad
        payload = ece_payoad.build_ece_program_payload(wa_id)   
    elif button_reply_id[3] == "b":
        from payload.ug.fet.se.sub import eee_payoad
        payload = eee_payoad.build_eee_program_payload(wa_id)
    elif button_reply_id[3] == "c":
        from payload.ug.fet.se.sub import ra_payoad
        payload = ra_payoad.build_ra_program_payload(wa_id) 
    elif button_reply_id[3] == "d":
        from payload.ug.fet.se.sub import ed_payoad
        payload = ed_payoad.build_ed_program_payload(wa_id) 
    elif button_reply_id[3] == "e":
        from payload.ug.fet.se.sub import ce_payoad
        payload = ce_payoad.build_ce_program_payload(wa_id) 
    elif button_reply_id[3] == "f":
        from payload.ug.fet.se.sub import bt_payoad
        payload = bt_payoad.build_bt_program_payload(wa_id) 
    elif button_reply_id[3] == "g":
        from payload.ug.fet.se.sub import me_payoad
        payload = me_payoad.build_me_program_payload(wa_id)
    elif button_reply_id[3] == "h":
        from payload.ug.fet.se.sub import evn_eee
        payload = evn_eee.build_eee_evening_program_payload(wa_id) 
    elif button_reply_id[3] == "i":
        from payload.ug.fet.se.sub import evn_civil
        payload = evn_civil.build_ce_evening_program_payload(wa_id)
    return _post_to_meta(payload)

def send_aabXX_details(wa_id, button_reply_id):
    """Send the details for the first course option based on the button reply ID."""
    if button_reply_id[3] == "a":
        send_ece.send_aabaX_details(wa_id, button_reply_id)
    elif button_reply_id[3] == "b":
        send_eee.send_aabbX_details(wa_id, button_reply_id)
    elif button_reply_id[3] == "c":
        send_ra.send_aabcX_details(wa_id, button_reply_id)
    elif button_reply_id[3] == "d":
        send_ed.send_aabdX_details(wa_id, button_reply_id)  
    elif button_reply_id[3] == "e":
        send_ce.send_aabeX_details(wa_id, button_reply_id) 
    elif button_reply_id[3] == "f":
        send_bt.send_aabfX_details(wa_id, button_reply_id) 
    elif button_reply_id[3] == "g":
        send_me.send_aabgX_details(wa_id, button_reply_id) 
   

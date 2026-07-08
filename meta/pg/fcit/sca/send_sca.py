from meta.client import _post_to_meta
from payload.pg.fcit.sca.sub import (mcaai_payoad,
                                     mcacy_payoad,
                                     mcads_payoad,
                                     mcag_payoad,
                                     mscai_payoad,
                                     msccy_payoad,
                                     mscds_payoad
                                     )
from meta.pg.fcit.sca.sub import (aida,
                                  cy,
                                  ds,
                                  gen,
                                  maida,
                                  mcy,
                                  mds
                                  )

def send_bcaX_details(wa_id, button_reply_id):
    """Send the details for the first course option based on the button reply ID."""
    if button_reply_id[3] == "a":
        payload = mcag_payoad.build_mca_program_payload(wa_id)     
    elif button_reply_id[3] == "b":
        payload = mcads_payoad.build_mca_data_science_program_payload(wa_id)  
    elif button_reply_id[3] == "c":
        payload = mcacy_payoad.build_mca_cyber_security_program_payload(wa_id)  
    elif button_reply_id[3] == "d":
        payload = mcaai_payoad.build_mca_ai_data_analytics_program_payload(wa_id)  
    elif button_reply_id[3] == "e":
        payload = mscds_payoad.build_msc_data_science_program_payload(wa_id)  
    elif button_reply_id[3] == "f":
        payload = mscai_payoad.build_msc_ai_data_analytics_program_payload(wa_id)  
    elif button_reply_id[3] == "g":
        payload = msccy_payoad.build_msc_cyber_security_program_payload(wa_id)  
    return _post_to_meta(payload)

def send_bcaXX_details(wa_id, button_reply_id):
    """Send the details for the first course option based on the button reply ID."""
    if button_reply_id[3] == "a":
        gen.send_bcaaX_details(wa_id, button_reply_id)
    elif button_reply_id[3] == "b":
        ds.send_bcabX_details(wa_id, button_reply_id)
    elif button_reply_id[3] == "c":
        cy.send_bcacX_details(wa_id, button_reply_id)
    elif button_reply_id[3] == "d":
        aida.send_bcadX_details(wa_id, button_reply_id)  
    elif button_reply_id[3] == "e":
        mds.send_bcaeX_details(wa_id, button_reply_id) 
    elif button_reply_id[3] == "f":
        maida.send_bcafX_details(wa_id, button_reply_id) 
    elif button_reply_id[3] == "g":
        mcy.send_bcagX_details(wa_id, button_reply_id) 
   

from meta.client import _post_to_meta
from payload.pg.gmsas.sub import (gsaeic_payoad,
                                  gsai_payoad,
                                  gsbgt_payoad,
                                  gsca_payoad,
                                  gsde_payoad,
                                  gsdl_payoad,
                                  gsisi_payoad,
                                  gspdm_payoad,
                                  gssess_payoad,
                                  gssga_payoad,
                                  gsstcd_payoad
                                  )
from meta.pg.gmsas.sub import (aeic,
                               aih,
                               bgt,
                               case,
                               de,
                               dl,
                               isi,
                               pdm,
                               sess,
                               sga,
                               stcd
                               )

def send_baXX_details(wa_id, button_reply_id):
    """Send the details for the first course option based on the button reply ID."""
    if button_reply_id[3] == "a":
        payload = gsdl_payoad.build_mtech_deep_learning_program_payload(wa_id)
    elif button_reply_id[3] == "b":
        payload = gsai_payoad.build_mtech_aih_program_payload(wa_id)   
    elif button_reply_id[3] == "c":
        payload = gsde_payoad.build_mtech_de_program_payload(wa_id)
    elif button_reply_id[3] == "d":
        payload = gsca_payoad.build_mtech_case_program_payload(wa_id)
    elif button_reply_id[3] == "e":
        payload = gssess_payoad.build_mtech_sesse_program_payload(wa_id)
    elif button_reply_id[3] == "f":
        payload = gsaeic_payoad.build_mtech_aeics_program_payload(wa_id)
    elif button_reply_id[3] == "g":
        payload = gsbgt_payoad.build_mtech_bgt_program_payload(wa_id)
    elif button_reply_id[3] == "h":
        payload = gspdm_payoad.build_mtech_pdm_program_payload(wa_id)
    elif button_reply_id[3] == "i":
        payload = gssga_payoad.build_mtech_sga_program_payload(wa_id)
    elif button_reply_id[3] == "j":
        payload = gsisi_payoad.build_mtech_isiiot_program_payload(wa_id)
    elif button_reply_id[3] == "k":
        payload = gsstcd_payoad.build_mtech_stcd_program_payload(wa_id)
    return _post_to_meta(payload)
    
def send_baXXX_details(wa_id, button_reply_id):
    if button_reply_id[3] == "a":
        dl.send_baaaX_details(wa_id, button_reply_id)
    elif button_reply_id[3] == "b":
        aih.send_baabX_details(wa_id, button_reply_id)
    elif button_reply_id[3] == "c":
       de.send_baacX_details(wa_id, button_reply_id)
    elif button_reply_id[3] == "d":
        case.send_baadX_details(wa_id, button_reply_id)
    elif button_reply_id[3] == "e":
        sess.send_baaeX_details(wa_id, button_reply_id)
    elif button_reply_id[3] == "f":
        aeic.send_baafX_details(wa_id, button_reply_id)
    elif button_reply_id[3] == "g":
        bgt.send_baagX_details(wa_id, button_reply_id)
    elif button_reply_id[3] == "h":
        pdm.send_baahX_details(wa_id, button_reply_id)
    elif button_reply_id[3] == "i":
        sga.send_baaiX_details(wa_id, button_reply_id)
    elif button_reply_id[3] == "j":
        isi.send_baajX_details(wa_id, button_reply_id)
    elif button_reply_id[3] == "k":
        stcd.send_baakX_details(wa_id, button_reply_id)

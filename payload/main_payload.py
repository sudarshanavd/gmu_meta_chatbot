from schema.service_schema import (WhatsAppInteractiveButtonRequest, 
                                   InteractiveButton, 
                                   MessageBody, MessageHeader, 
                                   MessageFooter, ButtonAction,
                                   Button,ButtonReply,
                                   WhatsAppInteractiveListRequest,
                                   ListSection, ListRow, ListAction,InteractiveList,
                                   WhatsAppTextReplyRequest, TextBody
)

def build_main_reply_payload(wa_id: str):
    """Builds the payload for the main reply message with buttons."""

    header = MessageHeader(
        text="🎓 GM University Admissions 2026-27"
    )

    body = MessageBody(
        text=(
            "Welcome to *GM University Admissions Helpdesk* 👋\n\n"
            "Explore academic programs, fee details, scholarships, "
            "placements, and campus opportunities.\n\n"
            "Please select an option below 👇"
        )
    )

    footer = MessageFooter(
        text="📍 GM University | Empowering Future Innovators"
    )

    btn_ug = Button(
        reply=ButtonReply(
            id="a",
            title="UG Programs"
        )
    )

    btn_pg = Button(
        reply=ButtonReply(
            id="b",
            title="PG Programs"
        )
    )

    btn_site = Button(
        reply=ButtonReply(
            id="c",
            title="Visit Website"
        )
    )

    action = ButtonAction(
        buttons=[btn_ug, btn_pg, btn_site]
    )

    interactive = InteractiveButton(
        header=header,
        body=body,
        footer=footer,
        action=action,
    )

    payload = WhatsAppInteractiveButtonRequest(
        to=wa_id,
        interactive=interactive
    )

    return payload.model_dump()




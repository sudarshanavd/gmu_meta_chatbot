from schema.service_schema import (WhatsAppInteractiveButtonRequest, 
                                   InteractiveButton, 
                                   MessageBody, MessageHeader, 
                                   MessageFooter, ButtonAction,
                                   Button,ButtonReply,
                                   WhatsAppInteractiveListRequest,
                                   ListSection, ListRow, ListAction,InteractiveList,
                                   WhatsAppTextReplyRequest, TextBody
)

def build_engineering_faculty_payload(wa_id: str):
    """Builds the payload for selecting the engineering faculty."""

    header = MessageHeader(
        text="🏫 Faculty of Engineering & Technology"
    )

    body = MessageBody(
        text=(
            "Welcome to the *Engineering Programs* section at "
            "*GM University* 👋\n\n"
            "Explore innovative and industry-focused engineering branches "
            "designed to prepare students for future technologies and careers.\n\n"
            "Please select your preferred faculty/department below 👇"
        )
    )

    footer = MessageFooter(
        text="🎓 GM University Admissions 2026-27"
    )

    btn_engineering_tech = Button(reply=ButtonReply(id="aaa", title="Engineering & Tech"))
    btn_school_engineering = Button(reply=ButtonReply(id="aab", title="School of Engg"))

    action = ButtonAction(buttons=[btn_engineering_tech, btn_school_engineering])

    interactive = InteractiveButton(
        header=header,
        body=body,
        footer=footer,
        action=action,
    )

    payload = WhatsAppInteractiveButtonRequest(to=wa_id, interactive=interactive)
    return payload.model_dump()
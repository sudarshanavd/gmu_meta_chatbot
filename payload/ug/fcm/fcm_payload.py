from schema.service_schema import (WhatsAppInteractiveButtonRequest, 
                                   InteractiveButton, 
                                   MessageBody, MessageHeader, 
                                   MessageFooter, ButtonAction,
                                   Button,ButtonReply,
                                   WhatsAppInteractiveListRequest,
                                   ListSection, ListRow, ListAction,InteractiveList,
                                   WhatsAppTextReplyRequest, TextBody
)

def build_commerce_faculty_payload(wa_id: str):
    """Builds the payload for selecting the commerce and management faculty."""

    header = MessageHeader(
        text="🏫 Faculty of Commerce & Management"
    )

    body = MessageBody(
        text=(
            "Welcome to the *Commerce & Management Programs* section at "
            "*GM University* 👋\n\n"
            "Explore business-focused programs designed for careers in "
            "commerce, analytics, finance, entrepreneurship, and management.\n\n"
            "Please select your preferred school below 👇"
        )
    )

    footer = MessageFooter(
        text="🎓 GM University Admissions 2026-27"
    )

    btn_school_commerce = Button(reply=ButtonReply(id="aba", title="School Commerce"))
    btn_school_management = Button(reply=ButtonReply(id="abb", title="School Mgmt"))

    action = ButtonAction(buttons=[btn_school_commerce, btn_school_management])

    interactive = InteractiveButton(
        header=header,
        body=body,
        footer=footer,
        action=action,
    )

    payload = WhatsAppInteractiveButtonRequest(to=wa_id, interactive=interactive)
    return payload.model_dump()

from schema.service_schema import (WhatsAppInteractiveButtonRequest, 
                                   InteractiveButton, 
                                   MessageBody, MessageHeader, 
                                   MessageFooter, ButtonAction,
                                   Button,ButtonReply,
                                   WhatsAppInteractiveListRequest,
                                   ListSection, ListRow, ListAction,InteractiveList,
                                   WhatsAppTextReplyRequest, TextBody
)

def build_computing_faculty_payload(wa_id: str):
    """Builds the payload for selecting the computing and IT faculty."""

    header = MessageHeader(
        text="💻 Faculty of Computing & IT"
    )

    body = MessageBody(
        text=(
            "Welcome to the *Computing & IT Programs* section at "
            "*GM University* 👋\n\n"
            "Explore computing-focused programs designed for careers in "
            "software, data science, cyber security, and AI.\n\n"
            "Please select your preferred school below 👇"
        )
    )

    footer = MessageFooter(
        text="🎓 GM University Admissions 2026-27"
    )

    btn_school_application = Button(reply=ButtonReply(id="aea", title="Computer App"))
    btn_school_science = Button(reply=ButtonReply(id="aeb", title="Computer Science"))

    action = ButtonAction(buttons=[btn_school_application, btn_school_science])

    interactive = InteractiveButton(
        header=header,
        body=body,
        footer=footer,
        action=action,
    )

    payload = WhatsAppInteractiveButtonRequest(to=wa_id, interactive=interactive)
    return payload.model_dump()

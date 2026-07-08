from schema.service_schema import (WhatsAppInteractiveButtonRequest, 
                                   InteractiveButton, 
                                   MessageBody, MessageHeader, 
                                   MessageFooter, ButtonAction,
                                   Button,ButtonReply,
                                   WhatsAppInteractiveListRequest,
                                   ListSection, ListRow, ListAction,InteractiveList,
                                   WhatsAppTextReplyRequest, TextBody
)

def build_science_faculty_payload(wa_id: str):
    """Builds the payload for selecting the basic and applied sciences faculty."""

    header = MessageHeader(
        text="🔬 Faculty of Basic & Applied Sciences"
    )

    body = MessageBody(
        text=(
            "Welcome to the *Basic & Applied Sciences Programs* section at "
            "*GM University* 👋\n\n"
            "Explore science-focused programs across mathematics, physical "
            "sciences, chemical and biological sciences, and applied sciences.\n\n"
            "Please select your preferred school below 👇"
        )
    )

    footer = MessageFooter(
        text="🎓 GM University Admissions 2026-27"
    )

    btn_math_physical = Button(reply=ButtonReply(id="ada", title="Math & Physical"))
    btn_chemical_bio = Button(reply=ButtonReply(id="adb", title="Chemical & Bio"))
    btn_applied_sciences = Button(reply=ButtonReply(id="adc", title="Applied Sciences"))

    action = ButtonAction(buttons=[btn_math_physical, btn_chemical_bio, btn_applied_sciences])

    interactive = InteractiveButton(
        header=header,
        body=body,
        footer=footer,
        action=action,
    )

    payload = WhatsAppInteractiveButtonRequest(to=wa_id, interactive=interactive)
    return payload.model_dump()

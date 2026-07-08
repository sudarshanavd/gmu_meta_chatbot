from schema.service_schema import (WhatsAppInteractiveButtonRequest, 
                                   InteractiveButton, 
                                   MessageBody, MessageHeader, 
                                   MessageFooter, ButtonAction,
                                   Button,ButtonReply,
                                   WhatsAppInteractiveListRequest,
                                   ListSection, ListRow, ListAction,InteractiveList,
                                   WhatsAppTextReplyRequest, TextBody
)

def build_school_of_computer_application_payload(wa_id: str):
    """Builds the payload for School of Computer Application programs."""

    header = MessageHeader(
        text="🖥️ School of Computer Application"
    )

    body = MessageBody(
        text=(
            "Welcome to the *School of Computer Application* 👋\n\n"
            "Explore application-focused computing programs designed for "
            "software, systems, and technology careers.\n\n"
            "Please choose the program you are interested in 👇"
        )
    )

    footer = MessageFooter(
        text="🎓 GM University Admissions 2026-27"
    )

    sections = [
        ListSection(
            title="Computer App Programs",
            rows=[
                ListRow(
                    id="aeaa",
                    title="General",
                    description="BCA"
                )
            ]
        )
    ]

    action = ListAction(button="Choose Program", sections=sections)

    interactive = InteractiveList(
        header=header,
        body=body,
        footer=footer,
        action=action,
    )

    payload = WhatsAppInteractiveListRequest(to=wa_id, interactive=interactive)
    return payload.model_dump()

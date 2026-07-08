from schema.service_schema import (WhatsAppInteractiveButtonRequest, 
                                   InteractiveButton, 
                                   MessageBody, MessageHeader, 
                                   MessageFooter, ButtonAction,
                                   Button,ButtonReply,
                                   WhatsAppInteractiveListRequest,
                                   ListSection, ListRow, ListAction,InteractiveList,
                                   WhatsAppTextReplyRequest, TextBody
)

def build_school_of_computer_science_payload(wa_id: str):
    """Builds the payload for School of Computer Science programs."""

    header = MessageHeader(
        text="💻 School of Computer Science"
    )

    body = MessageBody(
        text=(
            "Welcome to the *School of Computer Science* 👋\n\n"
            "Explore BCA specializations designed for careers in data science, "
            "cyber security, artificial intelligence, and analytics.\n\n"
            "Please choose the program/specialization you are interested in 👇"
        )
    )

    footer = MessageFooter(
        text="🎓 GM University Admissions 2026-27"
    )

    sections = [
        ListSection(
            title="Computer Science Programs",
            rows=[
                ListRow(
                    id="aeba",
                    title="Data Science",
                    description="BCA Data Science"
                ),
                ListRow(
                    id="aebb",
                    title="Cyber Security",
                    description="BCA Cyber Security"
                ),
                ListRow(
                    id="aebc",
                    title="AI & Data Analytics",
                    description="BCA AI and Data Analytics"
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

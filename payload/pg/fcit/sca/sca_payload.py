from schema.service_schema import (WhatsAppInteractiveButtonRequest, 
                                   InteractiveButton, 
                                   MessageBody, MessageHeader, 
                                   MessageFooter, ButtonAction,
                                   Button,ButtonReply,
                                   WhatsAppInteractiveListRequest,
                                   ListSection, ListRow, ListAction,InteractiveList,
                                   WhatsAppTextReplyRequest, TextBody
)

def build_pg_school_of_computer_application_payload(wa_id: str):
    """Builds the payload for PG School of Computer Application programs."""

    header = MessageHeader(
        text="🖥️ School of Computer Application"
    )

    body = MessageBody(
        text=(
            "Welcome to the *PG School of Computer Application* 👋\n\n"
            "Explore MCA and M.Sc New Age programs designed for advanced "
            "computing, data, cyber security, and AI careers.\n\n"
            "Please choose the program/specialization you are interested in 👇"
        )
    )

    footer = MessageFooter(
        text="🎓 GM University Admissions 2026-27"
    )

    sections = [
        ListSection(
            title="MCA Programs",
            rows=[
                ListRow(
                    id="bcaa",
                    title="General",
                    description="MCA General"
                ),
                ListRow(
                    id="bcab",
                    title="Data Science",
                    description="MCA Data Science"
                ),
                ListRow(
                    id="bcac",
                    title="Cyber Security",
                    description="MCA Cyber Security"
                ),
                ListRow(
                    id="bcad",
                    title="AI & Data Analytics",
                    description="MCA AI and Data Analytics"
                )
            ]
        ),
        ListSection(
            title="M.Sc New Age Programs",
            rows=[
                ListRow(
                    id="bcae",
                    title="Data Science",
                    description="M.Sc Data Science"
                ),
                ListRow(
                    id="bcaf",
                    title="AI & Data Analytics",
                    description="M.Sc AI and Data Analytics"
                ),
                ListRow(
                    id="bcag",
                    title="Cyber Security",
                    description="M.Sc Cyber Security"
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

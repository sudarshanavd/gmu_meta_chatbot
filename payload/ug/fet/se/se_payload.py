from schema.service_schema import (WhatsAppInteractiveButtonRequest, 
                                   InteractiveButton, 
                                   MessageBody, MessageHeader, 
                                   MessageFooter, ButtonAction,
                                   Button,ButtonReply,
                                   WhatsAppInteractiveListRequest,
                                   ListSection, ListRow, ListAction,InteractiveList,
                                   WhatsAppTextReplyRequest, TextBody
)

def build_school_of_engineering_payload(wa_id: str):
    """Builds the payload for School of Engineering programs."""

    header = MessageHeader(
        text="⚙️ School of Engineering"
    )

    body = MessageBody(
        text=(
            "Welcome to the *School of Engineering* 👋\n\n"
            "Explore core engineering programs designed for innovation, "
            "industry readiness, and future-focused careers.\n\n"
            "Please choose the program/specialization you are interested in 👇"
        )
    )

    footer = MessageFooter(
        text="🎓 GM University Admissions 2026-27"
    )

    sections = [
        ListSection(
            title="Engineering Programs",
            rows=[
                ListRow(
                    id="aaba",
                    title="Electronics & Comm",
                    description="B.Tech E&CE"
                ),
                ListRow(
                    id="aabb",
                    title="Electrical & Electronics",
                    description="B.Tech EEE"
                ),
                ListRow(
                    id="aabc",
                    title="Robotics & Automation",
                    description="B.Tech RA"
                ),
                ListRow(
                    id="aabd",
                    title="Engineering Design",
                    description="B.Tech ED"
                ),
                ListRow(
                    id="aabe",
                    title="Civil Engineering",
                    description="B.Tech CE"
                ),
                ListRow(
                    id="aabf",
                    title="Biotechnology",
                    description="B.Tech BT"
                ),
                ListRow(
                    id="aabg",
                    title="Mechanical Engineering",
                    description="B.Tech ME"
                )
            ]
        ),
        ListSection(
            title="Evening Courses",
            rows=[
                ListRow(
                    id="aabh",
                    title="Electrical & Elec Eve",
                    description="Electrical and Electronics Engineering (Evening)"
                ),
                ListRow(
                    id="aabi",
                    title="Civil Engg Evening",
                    description="Civil Engineering (Evening)"
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

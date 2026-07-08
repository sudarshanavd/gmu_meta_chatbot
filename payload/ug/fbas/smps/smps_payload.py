from schema.service_schema import (WhatsAppInteractiveButtonRequest, 
                                   InteractiveButton, 
                                   MessageBody, MessageHeader, 
                                   MessageFooter, ButtonAction,
                                   Button,ButtonReply,
                                   WhatsAppInteractiveListRequest,
                                   ListSection, ListRow, ListAction,InteractiveList,
                                   WhatsAppTextReplyRequest, TextBody
)

def build_school_of_mathematical_physical_sciences_payload(wa_id: str):
    """Builds the payload for School of Mathematical and Physical Sciences programs."""

    header = MessageHeader(
        text="📐 School of Mathematical & Physical Sciences"
    )

    body = MessageBody(
        text=(
            "Welcome to the *School of Mathematical & Physical Sciences* 👋\n\n"
            "Explore science programs designed for careers in physics, "
            "mathematics, statistics, computing, and analytics.\n\n"
            "Please choose the program/specialization you are interested in 👇"
        )
    )

    footer = MessageFooter(
        text="🎓 GM University Admissions 2026-27"
    )

    sections = [
        ListSection(
            title="Math & Physical Programs",
            rows=[
                ListRow(
                    id="adaa",
                    title="Physics, Mathematics",
                    description="B.Sc Physics, Mathematics"
                ),
                ListRow(
                    id="adab",
                    title="Mathematics, CS",
                    description="B.Sc Mathematics, Computer Science"
                ),
                ListRow(
                    id="adac",
                    title="Statistics, CS",
                    description="B.Sc Statistics, Computer Science"
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

from schema.service_schema import (WhatsAppInteractiveButtonRequest, 
                                   InteractiveButton, 
                                   MessageBody, MessageHeader, 
                                   MessageFooter, ButtonAction,
                                   Button,ButtonReply,
                                   WhatsAppInteractiveListRequest,
                                   ListSection, ListRow, ListAction,InteractiveList,
                                   WhatsAppTextReplyRequest, TextBody
)

def build_school_of_applied_sciences_payload(wa_id: str):
    """Builds the payload for School of Applied Sciences programs."""

    header = MessageHeader(
        text="🔬 School of Applied Sciences"
    )

    body = MessageBody(
        text=(
            "Welcome to the *School of Applied Sciences* 👋\n\n"
            "Explore applied science programs designed for food technology, "
            "biotechnology, tissue engineering, and microbiology careers.\n\n"
            "Please choose the program/specialization you are interested in 👇"
        )
    )

    footer = MessageFooter(
        text="🎓 GM University Admissions 2026-27"
    )

    sections = [
        ListSection(
            title="Applied Sciences Programs",
            rows=[
                ListRow(
                    id="adca",
                    title="Food Science & Tech",
                    description="B.Sc Food Science and Technology"
                ),
                ListRow(
                    id="adcb",
                    title="Biotech & Tissue Engg",
                    description="B.Sc Biotechnology and Tissue Engineering"
                ),
                ListRow(
                    id="adcc",
                    title="Industrial Microbio",
                    description="B.Sc Industrial Microbiology"
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

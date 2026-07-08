from schema.service_schema import (WhatsAppInteractiveButtonRequest, 
                                   InteractiveButton, 
                                   MessageBody, MessageHeader, 
                                   MessageFooter, ButtonAction,
                                   Button,ButtonReply,
                                   WhatsAppInteractiveListRequest,
                                   ListSection, ListRow, ListAction,InteractiveList,
                                   WhatsAppTextReplyRequest, TextBody
)

def build_pg_fbas_payload(wa_id: str):
    """Builds the payload for PG Faculty of Basic and Applied Sciences programs."""

    header = MessageHeader(
        text="🔬 Faculty of Basic & Applied Sciences"
    )

    body = MessageBody(
        text=(
            "Welcome to the *PG Faculty of Basic & Applied Sciences* 👋\n\n"
            "Explore M.Sc programs designed for advanced study in science, "
            "mathematics, and food technology.\n\n"
            "Please choose the program you are interested in 👇"
        )
    )

    footer = MessageFooter(
        text="🎓 GM University Admissions 2026-27"
    )

    sections = [
        ListSection(
            title="M.Sc Programs",
            rows=[
                ListRow(
                    id="bbaa",
                    title="Physics",
                    description="M.Sc Physics"
                ),
                ListRow(
                    id="bbab",
                    title="Chemistry",
                    description="M.Sc Chemistry"
                ),
                ListRow(
                    id="bbac",
                    title="Mathematics",
                    description="M.Sc Mathematics"
                ),
                ListRow(
                    id="bbad",
                    title="Food Technology",
                    description="M.Sc Food Technology"
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

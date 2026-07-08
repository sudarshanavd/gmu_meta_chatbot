from schema.service_schema import (WhatsAppInteractiveButtonRequest, 
                                   InteractiveButton, 
                                   MessageBody, MessageHeader, 
                                   MessageFooter, ButtonAction,
                                   Button,ButtonReply,
                                   WhatsAppInteractiveListRequest,
                                   ListSection, ListRow, ListAction,InteractiveList,
                                   WhatsAppTextReplyRequest, TextBody
)

def build_gmbs_payload(wa_id: str):
    """Builds the payload for GM Business School PG programs."""

    header = MessageHeader(
        text="🏫 GM Business School"
    )

    body = MessageBody(
        text=(
            "Welcome to the *GM Business School* 👋\n\n"
            "Explore MBA programs designed for management, leadership, "
            "professional growth, and global business careers.\n\n"
            "Please choose the program you are interested in 👇"
        )
    )

    footer = MessageFooter(
        text="🎓 GM University Admissions 2026-27"
    )

    sections = [
        ListSection(
            title="MBA Programs",
            rows=[
                ListRow(
                    id="beaa",
                    title="General",
                    description="MBA General"
                ),
                ListRow(
                    id="beab",
                    title="Professional",
                    description="MBA Professional"
                ),
                ListRow(
                    id="beac",
                    title="Advanced",
                    description="MBA Advanced"
                ),
                ListRow(
                    id="bead",
                    title="International",
                    description="MBA International"
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

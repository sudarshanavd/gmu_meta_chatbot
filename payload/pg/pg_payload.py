from schema.service_schema import (WhatsAppInteractiveButtonRequest, 
                                   InteractiveButton, 
                                   MessageBody, MessageHeader, 
                                   MessageFooter, ButtonAction,
                                   Button,ButtonReply,
                                   WhatsAppInteractiveListRequest,
                                   ListSection, ListRow, ListAction,InteractiveList,
                                   WhatsAppTextReplyRequest, TextBody
)

def build_pg_details_payload(wa_id: str):
    """Builds the payload for PG programs list message."""

    header = MessageHeader(
        text="🎓 Postgraduate Programs"
    )

    body = MessageBody(
        text=(
            "Explore the *Postgraduate Programs* offered at "
            "*GM University*.\n\n"
            "Select a category to view available specializations.\n\n"
            "Please choose a program below 👇"
        )
    )

    footer = MessageFooter(
        text="📍 GM University | Inspiring Transformation"
    )

    sections = [
        ListSection(
        title="PG Faculties",
        rows=[
            ListRow(
                id="aa",
                title="Advanced Studies",
                description="M.Tech Programs"
            ),
            ListRow(
                id="bb",
                title="Basic & Applied Sciences",
                description="M.Sc Programs"
            ),
            ListRow(
                id="bc",
                title="Computing & IT",
                description="MCA & M.Sc (New Age)"
            ),
            ListRow(
                id="bd",
                title="Commerce & Management",
                description="M.Com Programs"
            ),
            ListRow(
                id="be",
                title="GM Business School",
                description="MBA Programs"
            ),
            ListRow(
                id="bf",
                title="PG Diploma",
                description="AI, IoT, Embedded Systems"
            )
        ]
    )
    ]

    action = ListAction(
        button="Choose Program",
        sections=sections
    )

    interactive = InteractiveList(
        header=header,
        body=body,
        footer=footer,
        action=action,
    )

    payload = WhatsAppInteractiveListRequest(
        to=wa_id,
        interactive=interactive
    )

    return payload.model_dump()
from schema.service_schema import (WhatsAppInteractiveButtonRequest, 
                                   InteractiveButton, 
                                   MessageBody, MessageHeader, 
                                   MessageFooter, ButtonAction,
                                   Button,ButtonReply,
                                   WhatsAppInteractiveListRequest,
                                   ListSection, ListRow, ListAction,InteractiveList,
                                   WhatsAppTextReplyRequest, TextBody
)

def build_pgd_payload(wa_id: str):
    """Builds the payload for Post Graduate Diploma programs."""

    header = MessageHeader(
        text="📘 Post Graduate Diploma"
    )

    body = MessageBody(
        text=(
            "Welcome to the *Post Graduate Diploma* programs section 👋\n\n"
            "Explore skill-oriented PG diploma programs designed with "
            "industry-relevant technology and finance focus areas.\n\n"
            "Please choose the program you are interested in 👇"
        )
    )

    footer = MessageFooter(
        text="🎓 GM University Admissions 2026-27"
    )

    sections = [
        ListSection(
            title="PG Diploma Programs",
            rows=[
                ListRow(
                    id="bgaa",
                    title="AI & IoT",
                    description="PGD in AI and IoT with Intel"
                ),
                ListRow(
                    id="bgab",
                    title="Embedded Systems",
                    description="PGD in Embedded Systems with Texas Instruments"
                ),
                ListRow(
                    id="bgac",
                    title="Accounting & Finance",
                    description="PGD in Accounting and Finance with Tally"
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

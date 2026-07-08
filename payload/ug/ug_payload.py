from schema.service_schema import (WhatsAppInteractiveButtonRequest, 
                                   InteractiveButton, 
                                   MessageBody, MessageHeader, 
                                   MessageFooter, ButtonAction,
                                   Button,ButtonReply,
                                   WhatsAppInteractiveListRequest,
                                   ListSection, ListRow, ListAction,InteractiveList,
                                   WhatsAppTextReplyRequest, TextBody
)

def build_ug_details_payload(wa_id: str):
    """Builds the payload for UG programs list message."""

    header = MessageHeader(
        text="🎓 Undergraduate Programs"
    )

    body = MessageBody(
        text=(
            "Explore the wide range of *Undergraduate Programs* offered at "
            "*GM University*.\n\n"
            "Select the program you are interested in to view details such as:\n"
            "• Course Information\n"
            "• Eligibility\n"
            "• Fee Structure\n"
            "• Career Opportunities\n\n"
            "Please choose a program below 👇"
        )
    )

    footer = MessageFooter(
        text="📍 GM University | Shaping Future Leaders"
    )

    sections = [
        ListSection(
            title="Engineering & Technology",
            rows=[
                ListRow(
                    id="aa",
                    title="Engineering & Tech",
                    description="BTech, BE programs"
                )
            ]
        ),
        ListSection(
            title="Commerce & Management",
            rows=[
                ListRow(
                    id="ab",
                    title="Commerce & Mgmt",
                    description="BBA, BCom programs"
                ),
                ListRow(
                    id="ac",
                    title="GM School of Law",
                    description="BA.LLB, BBA.LLB programs"
                )
            ]
        ),
        ListSection(
            title="Science & Computing",
            rows=[
                ListRow(
                    id="ad",
                    title="Basic Sciences",
                    description="BSc programs"
                ),
                ListRow(
                    id="ae",
                    title="Computing & IT",
                    description="BTech CS, BCA programs"
                )
            ]
        ),
        ListSection(
            title="Specialized Programs",
            rows=[
                ListRow(
                    id="af",
                    title="Research Programs",
                    description="UG research opportunities"
                ),
                ListRow(
                    id="ag",
                    title="B.Voc.",
                    description="Vocational degree programs"
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
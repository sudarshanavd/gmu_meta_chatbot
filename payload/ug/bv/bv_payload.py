from schema.service_schema import (WhatsAppInteractiveButtonRequest, 
                                   InteractiveButton, 
                                   MessageBody, MessageHeader, 
                                   MessageFooter, ButtonAction,
                                   Button,ButtonReply,
                                   WhatsAppInteractiveListRequest,
                                   ListSection, ListRow, ListAction,InteractiveList,
                                   WhatsAppTextReplyRequest, TextBody
)

def build_b_voc_payload(wa_id: str):
    """Builds the payload for B.Voc. programs."""

    header = MessageHeader(
        text="🛠️ B.Voc. Programs"
    )

    body = MessageBody(
        text=(
            "Welcome to the *B.Voc. Programs* section at *GM University* 👋\n\n"
            "Explore skill-focused programs designed for industry readiness, "
            "entrepreneurship, and applied professional careers.\n\n"
            "Please choose the program you are interested in 👇"
        )
    )

    footer = MessageFooter(
        text="🎓 GM University Admissions 2026-27"
    )

    sections = [
        ListSection(
            title="B.Voc. Programs",
            rows=[
                ListRow(
                    id="agaa",
                    title="EV Technology",
                    description="B.Voc. in Electrical Vehicle Technology"
                ),
                ListRow(
                    id="agab",
                    title="Fashion & Apparel",
                    description="B.Voc. in Fashion Design and Apparel Manufacture"
                ),
                ListRow(
                    id="agac",
                    title="Drone Development",
                    description="B.Voc. in Drone Development and Application"
                ),
                ListRow(
                    id="agad",
                    title="Airport Ground Svcs",
                    description="B.Voc. in Airport Ground Services and Support"
                ),
                ListRow(
                    id="agae",
                    title="E-Commerce Marketing",
                    description="B.Voc. in E-Commerce and Digital Marketing"
                ),
                ListRow(
                    id="agaf",
                    title="Animation & VFX",
                    description="BSc in Animation and Visual Effects"
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

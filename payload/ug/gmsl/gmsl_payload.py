from schema.service_schema import (WhatsAppInteractiveButtonRequest, 
                                   InteractiveButton, 
                                   MessageBody, MessageHeader, 
                                   MessageFooter, ButtonAction,
                                   Button,ButtonReply,
                                   WhatsAppInteractiveListRequest,
                                   ListSection, ListRow, ListAction,InteractiveList,
                                   WhatsAppTextReplyRequest, TextBody
)

def build_law_faculty_payload(wa_id: str):
    """Builds the payload for GM School of Law programs."""

    header = MessageHeader(
        text="⚖️ GM School of Law"
    )

    body = MessageBody(
        text=(
            "Welcome to the *GM School of Law* 👋\n\n"
            "Explore law programs designed for legal practice, business law, "
            "commerce, policy, and public service careers.\n\n"
            "Please choose the program you are interested in 👇"
        )
    )

    footer = MessageFooter(
        text="🎓 GM University Admissions 2026-27"
    )

    sections = [
        ListSection(
            title="Law Programs",
            rows=[
                ListRow(
                    id="acaa",
                    title="LL.B.",
                    description="Bachelor of Laws"
                ),
                ListRow(
                    id="acab",
                    title="B.B.A., LL.B.",
                    description="Integrated Law Program"
                ),
                ListRow(
                    id="acac",
                    title="B.Com., LL.B.",
                    description="Integrated Law Program"
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

from schema.service_schema import (WhatsAppInteractiveButtonRequest, 
                                   InteractiveButton, 
                                   MessageBody, MessageHeader, 
                                   MessageFooter, ButtonAction,
                                   Button,ButtonReply,
                                   WhatsAppInteractiveListRequest,
                                   ListSection, ListRow, ListAction,InteractiveList,
                                   WhatsAppTextReplyRequest, TextBody
)

def build_research_programs_payload(wa_id: str):
    """Builds the payload for research programs."""

    header = MessageHeader(
        text="🎓 Research Programs"
    )

    body = MessageBody(
        text=(
            "Welcome to the *Research Programs* section at *GM University* 👋\n\n"
            "Explore PhD programs across engineering, computing, sciences, "
            "commerce, and management.\n\n"
            "Please choose the research area you are interested in 👇"
        )
    )

    footer = MessageFooter(
        text="🎓 GM University Admissions 2026-27"
    )

    sections = [
        ListSection(
            title="PhD Programs",
            rows=[
                ListRow(
                    id="afaa",
                    title="Engineering & Tech",
                    description="PhD Faculty of Engineering and Technology"
                ),
                ListRow(
                    id="afab",
                    title="Computing & IT",
                    description="PhD Faculty of Computing and IT"
                ),
                ListRow(
                    id="afac",
                    title="Basic & Applied Sci",
                    description="PhD Faculty of Basic and Applied Sciences"
                ),
                ListRow(
                    id="afad",
                    title="Commerce & Mgmt",
                    description="PhD Faculty of Commerce and Management"
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

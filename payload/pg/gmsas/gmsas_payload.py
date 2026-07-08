from schema.service_schema import (WhatsAppInteractiveButtonRequest, 
                                   InteractiveButton, 
                                   MessageBody, MessageHeader, 
                                   MessageFooter, ButtonAction,
                                   Button,ButtonReply,
                                   WhatsAppInteractiveListRequest,
                                   ListSection, ListRow, ListAction,InteractiveList,
                                   WhatsAppTextReplyRequest, TextBody
)

def build_gmsas_payload(wa_id: str):
    """Builds the payload for GM School of Advanced Studies PG programs."""

    header = MessageHeader(
        text="🎓 GM School of Advanced Studies"
    )

    body = MessageBody(
        text=(
            "Welcome to the *GM School of Advanced Studies* 👋\n\n"
            "Explore M.Tech programs designed for advanced careers in AI, "
            "data engineering, electronics, sustainability, IoT, and chip design.\n\n"
            "Please choose the specialization you are interested in 👇"
        )
    )

    footer = MessageFooter(
        text="🎓 GM University Admissions 2026-27"
    )

    sections = [
        ListSection(
            title="M.Tech Programs",
            rows=[
                ListRow(
                    id="baaa",
                    title="Deep Learning",
                    description="M.Tech Deep Learning"
                ),
                ListRow(
                    id="baab",
                    title="AI in Healthcare",
                    description="M.Tech AI in Healthcare"
                ),
                ListRow(
                    id="baac",
                    title="Data Engineering",
                    description="M.Tech Data Engineering"
                ),
                ListRow(
                    id="baaf",
                    title="CASE",
                    description="Computer Aided Structural Engineering"
                ),
                ListRow(
                    id="baae",
                    title="Smart Electrical",
                    description="Smart Electrical Systems and Sustainable Energy"
                ),
                ListRow(
                    id="baag",
                    title="Advanced Electronics",
                    description="Advanced Electronics and Intelligent Communication Systems"
                ),
                ListRow(
                    id="baah",
                    title="Bioengineering",
                    description="Bioengineering and Genetic Technology"
                ),
                ListRow(
                    id="baai",
                    title="Product Development",
                    description="Product Development and Marketing"
                ),
                ListRow(
                    id="baaj",
                    title="Smart Agriculture",
                    description="Smart and Green Agriculture"
                ),
                ListRow(
                    id="baak",
                    title="Industrial IoT",
                    description="Intelligent Systems and Industrial IoT"
                ),
                ListRow(
                    id="baal",
                    title="Semiconductor Tech",
                    description="Semiconductor Technologies and Chip Design"
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

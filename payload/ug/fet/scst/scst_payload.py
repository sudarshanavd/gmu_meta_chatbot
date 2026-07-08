from schema.service_schema import (WhatsAppInteractiveButtonRequest, 
                                   InteractiveButton, 
                                   MessageBody, MessageHeader, 
                                   MessageFooter, ButtonAction,
                                   Button,ButtonReply,
                                   WhatsAppInteractiveListRequest,
                                   ListSection, ListRow, ListAction,InteractiveList,
                                   WhatsAppTextReplyRequest, TextBody
)
def build_cs_technology_list_payload(wa_id: str):
    """Builds the payload for School of Computer Science and Technology programs."""

    header = MessageHeader(
        text="💻 School of Computer Science & Technology"
    )

    body = MessageBody(
        text=(
            "Welcome to the *School of Computer Science & Technology* 👋\n\n"
            "Discover cutting-edge programs designed for careers in:\n\n"
            "Please choose the program/specialization you are interested in 👇"
        )
    )

    footer = MessageFooter(
        text="🎓 GM University Admissions 2026-27"
    )

    sections = [
        ListSection(
            title="CS & Technology Programs",
            rows=[
                ListRow(
                    id="aaaa",
                    title="Computer Science & Engg",
                    description="B.Tech CSE"
                ),
                ListRow(
                    id="aaab",
                    title="Information Science",
                    description="B.Tech ISE"
                ),
                ListRow(
                    id="aaac",
                    title="CS - AI & ML",
                    description="B.Tech CS-AIML"
                ),
                ListRow(
                    id="aaad",
                    title="CS - AI, Blockchain",
                    description="B.Tech AI, BC & BS"
                ),
                ListRow(
                    id="aaae",
                    title="CS - IoT with AI",
                    description="B.Tech CS-IoT + AI"
                ),
                ListRow(
                    id="aaaf",
                    title="CS - Data Science",
                    description="B.Tech CS-DS"
                ),
                ListRow(
                    id="aaag",
                    title="CS - Cyber Security",
                    description="B.Tech CS-CY"
                ),
                ListRow(
                    id="aaah",
                    title="CS - Cloud Computing",
                    description="B.Tech CS-CC"
                ),
                ListRow(
                    id="aaai",
                    title="CS - Info Security",
                    description="B.Tech CS-IY"
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
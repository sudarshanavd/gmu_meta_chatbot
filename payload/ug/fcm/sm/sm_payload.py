from schema.service_schema import (WhatsAppInteractiveButtonRequest, 
                                   InteractiveButton, 
                                   MessageBody, MessageHeader, 
                                   MessageFooter, ButtonAction,
                                   Button,ButtonReply,
                                   WhatsAppInteractiveListRequest,
                                   ListSection, ListRow, ListAction,InteractiveList,
                                   WhatsAppTextReplyRequest, TextBody
)

def build_school_of_management_payload(wa_id: str):
    """Builds the payload for School of Management programs."""

    header = MessageHeader(
        text="📊 School of Management"
    )

    body = MessageBody(
        text=(
            "Welcome to the *School of Management* 👋\n\n"
            "Explore management programs designed for leadership, "
            "entrepreneurship, analytics, marketing, and service-sector careers.\n\n"
            "Please choose the program/specialization you are interested in 👇"
        )
    )

    footer = MessageFooter(
        text="🎓 GM University Admissions 2026-27"
    )

    sections = [
        ListSection(
            title="Management Programs",
            rows=[
                ListRow(
                    id="abba",
                    title="General",
                    description="BBA"
                ),
                ListRow(
                    id="abbb",
                    title="Blockchain & Fintech",
                    description="BBA Blockchain and Fintech"
                ),
                ListRow(
                    id="abbc",
                    title="AI & Business Analytics",
                    description="BBA AI and Business Analytics"
                ),
                ListRow(
                    id="abbd",
                    title="Digital Marketing",
                    description="BBA Digital Marketing and E-Commerce"
                ),
                ListRow(
                    id="abbe",
                    title="Aviation Management",
                    description="BBA Aviation Management"
                ),
                ListRow(
                    id="abbf",
                    title="Tourism & Hospitality",
                    description="BBA Tourism, Hospitality and Event Management"
                ),
                ListRow(
                    id="abbg",
                    title="Healthcare Management",
                    description="BBA Healthcare Management"
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

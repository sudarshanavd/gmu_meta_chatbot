from schema.service_schema import (WhatsAppInteractiveButtonRequest, 
                                   InteractiveButton, 
                                   MessageBody, MessageHeader, 
                                   MessageFooter, ButtonAction,
                                   Button,ButtonReply,
                                   WhatsAppInteractiveListRequest,
                                   ListSection, ListRow, ListAction,InteractiveList,
                                   WhatsAppTextReplyRequest, TextBody
)

def build_school_of_commerce_payload(wa_id: str):
    """Builds the payload for School of Commerce programs."""

    header = MessageHeader(
        text="💼 School of Commerce"
    )

    body = MessageBody(
        text=(
            "Welcome to the *School of Commerce* 👋\n\n"
            "Explore commerce programs designed for business, analytics, "
            "finance, and taxation careers.\n\n"
            "Please choose the program/specialization you are interested in 👇"
        )
    )

    footer = MessageFooter(
        text="🎓 GM University Admissions 2026-27"
    )

    sections = [
        ListSection(
            title="Commerce Programs",
            rows=[
                ListRow(
                    id="abaa",
                    title="General",
                    description="B.Com"
                ),
                ListRow(
                    id="abab",
                    title="Data Analytics & BI",
                    description="B.Com Data Analytics and Business Intelligence"
                ),
                ListRow(
                    id="abac",
                    title="AI & Business Analytics",
                    description="B.Com AI and Business Analytics"
                ),
                ListRow(
                    id="abad",
                    title="Accounting & Taxation",
                    description="B.Com Accounting and Taxation"
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

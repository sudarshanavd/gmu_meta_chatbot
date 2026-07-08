from schema.service_schema import (WhatsAppInteractiveButtonRequest, 
                                   InteractiveButton, 
                                   MessageBody, MessageHeader, 
                                   MessageFooter, ButtonAction,
                                   Button,ButtonReply,
                                   WhatsAppInteractiveListRequest,
                                   ListSection, ListRow, ListAction,InteractiveList,
                                   WhatsAppTextReplyRequest, TextBody
)

def build_school_of_chemical_biological_sciences_payload(wa_id: str):
    """Builds the payload for School of Chemical and Biological Sciences programs."""

    header = MessageHeader(
        text="🧪 School of Chemical & Biological Sciences"
    )

    body = MessageBody(
        text=(
            "Welcome to the *School of Chemical & Biological Sciences* 👋\n\n"
            "Explore science programs designed for careers in chemistry, "
            "biology, environmental science, and interdisciplinary research.\n\n"
            "Please choose the program/specialization you are interested in 👇"
        )
    )

    footer = MessageFooter(
        text="🎓 GM University Admissions 2026-27"
    )

    sections = [
        ListSection(
            title="Chemical & Bio Programs",
            rows=[
                ListRow(
                    id="adba",
                    title="Physics, Chemistry",
                    description="B.Sc Physics, Chemistry"
                ),
                ListRow(
                    id="adbb",
                    title="Chemistry, CS",
                    description="B.Sc Chemistry, Computer Science"
                ),
                ListRow(
                    id="adbc",
                    title="Chemistry, Zoology",
                    description="B.Sc Chemistry, Zoology"
                ),
                ListRow(
                    id="adbd",
                    title="Chemistry, Botany",
                    description="B.Sc Chemistry, Botany"
                ),
                ListRow(
                    id="adbe",
                    title="Chemistry, Env Science",
                    description="B.Sc Chemistry, Environmental Science"
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

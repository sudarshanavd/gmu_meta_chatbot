from schema.service_schema import (
    WhatsAppInteractiveButtonRequest,
    InteractiveButton,
    MessageHeader,
    MessageBody,
    MessageFooter,
    ButtonAction,
    Button,
    ButtonReply,
)

def build_pg_fcit_payload(wa_id: str):
    """Builds the payload for PG Faculty of Computing & IT with reply buttons."""

    header = MessageHeader(
        text="💻 Faculty of Computing & IT"
    )

    body = MessageBody(
        text=(
            "Welcome to the *PG Faculty of Computing & IT* 👋\n\n"
            "Explore postgraduate computing programs.\n\n"
            "Please choose a program 👇"
        )
    )

    footer = MessageFooter(
        text="🎓 GM University Admissions 2026-27"
    )

    btn_mca = Button(
        reply=ButtonReply(
            id="bca",
            title="MCA"
        )
    )

    btn_msc = Button(
        reply=ButtonReply(
            id="bcb",
            title="M.Sc New Age"
        )
    )

    action = ButtonAction(
        buttons=[
            btn_mca,
            btn_msc
        ]
    )

    interactive = InteractiveButton(
        header=header,
        body=body,
        footer=footer,
        action=action,
    )

    payload = WhatsAppInteractiveButtonRequest(
        to=wa_id,
        interactive=interactive
    )

    return payload.model_dump()
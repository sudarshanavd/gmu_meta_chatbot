from schema.service_schema import (
    WhatsAppInteractiveButtonRequest,
    InteractiveButton,
    MessageBody,
    MessageHeader,
    MessageFooter,
    ButtonAction,
    Button,
    ButtonReply,
    WhatsAppTextReplyRequest,
    TextBody
)

def build_ce_evening_program_payload(wa_id: str):
    """Builds the payload for the Civil Engineering (Evening) program."""

    header = MessageHeader(
        text="🏗️ Civil Engineering (Evening)"
    )

    body = MessageBody(
        text=(
            "🎓 *B.E. in Civil Engineering (Evening)*\n\n"
            "Learn core concepts in:\n"
            "• Structural Engineering\n"
            "• Construction Technology\n"
            "• Geotechnical Engineering\n"
            "• Transportation Engineering\n"
            "• Environmental Engineering\n"
            "• Surveying\n"
            "• Concrete Technology\n"
            "• Water Resources Engineering\n"
            "• Building Planning & Design\n"
            "• Project Management\n\n"
        )
    )

    footer = MessageFooter(
        text="🎓 GM University Admissions 2026-27"
    )

    # btn_program_details = Button(reply=ButtonReply(id="00101", title="Program Details"))
    # btn_fee_duration = Button(reply=ButtonReply(id="00102", title="Fee & Duration"))
    # # btn_branch_website = Button(reply=ButtonReply(id="00103", title="Branch Website"))

    # action = ButtonAction(
    #     # buttons=[btn_program_details, btn_fee_duration, btn_branch_website]
    #     buttons=[]
    # )

    # interactive = InteractiveButton(
    #     header=header,
    #     body=body,
    #     footer=footer,
    #     action= action,
    # )

    payload = WhatsAppTextReplyRequest(
        to=wa_id,
        text=TextBody(
            header = header.text,
            body=body.text,
            footer = footer.text,
            preview_url=True
        ),
    )

    return payload.model_dump()
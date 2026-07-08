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

def build_eee_evening_program_payload(wa_id: str):
    """Builds the payload for the Electrical and Electronics Engineering (Evening) program."""

    header = MessageHeader(
        text="⚡ Electrical & Electronics Engineering (Evening)"
    )

    body = MessageBody(
        text=(
            "🎓 *B.E. in Electrical & Electronics Engineering (Evening)*\n\n"
            "Learn core concepts in:\n"
            "• Electrical Circuits\n"
            "• Power Systems\n"
            "• Electrical Machines\n"
            "• Power Electronics\n"
            "• Control Systems\n"
            "• Digital Electronics\n"
            "• Renewable Energy Systems\n"
            "• Industrial Automation\n"
            "• High Voltage Engineering\n"
            "• Smart Grid Technologies\n\n"
        )
    )

    footer = MessageFooter(
        text="🎓 GM University Admissions 2026-27"
    )

    # btn_program_details = Button(reply=ButtonReply(id="00101", title="Program Details"))
    # btn_fee_duration = Button(reply=ButtonReply(id="00102", title="Fee & Duration"))
    # # btn_branch_website = Button(reply=ButtonReply(id="00103", title="Branch Website"))

    # action = ButtonAction(
    #     buttons=[btn_program_details, btn_fee_duration, btn_branch_website]
    #     buttons=[btn_program_details, btn_fee_duration, ]
    # )

    # interactive = InteractiveButton(
    #     header=header,
    #     body=body,
    #     footer=footer,
    #     # action=action,
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

# def build_eee_evening_program_details_payload(wa_id: str):
#     """Builds a well-formatted WhatsApp text payload for Electrical & Electronics Engineering (Evening) program details."""

#     text = (
#         "🎓 *B.E. Electrical & Electronics Engineering (Evening)*\n"
#         "📘 *Program Details – 2026-27 Intake*\n\n"

#         "━━━━━━━━━━━━━━━\n"
#         "📄 *Program Brochure Includes:*\n"
#         "• Curriculum Structure\n"
#         "• Eligibility Criteria\n"
#         "• Core EEE Subjects\n"
#         "• Laboratories & Facilities\n"
#         "• Department Highlights\n"
#         "• Academic & Career Opportunities\n"
#         "━━━━━━━━━━━━━━━\n\n"

#         "🔗 *View Full Program Brochure:*\n"
#         "https://gmu.ac.in/pdfview_assets%5Cdownloadmaterial%5CUG%20Programs%5Cprogram%5CPD_EEE_Evening_2026-27.pdf\n\n"

#         "📞 *Contact Details*\n"
#         "━━━━━━━━━━━━━━━\n"
#         "📍 GM University, Davangere\n"
#         "☎️ Phone: +91 XXXXX XXXXX\n"
#         "📧 Email: eee@gmu.ac.in\n"
#     )

#     payload = WhatsAppTextReplyRequest(
#         to=wa_id,
#         text=TextBody(
#             body=text,
#             preview_url=True
#         ),
#     )

#     return payload.model_dump()
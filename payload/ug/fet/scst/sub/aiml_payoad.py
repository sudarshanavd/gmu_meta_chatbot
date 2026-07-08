from schema.service_schema import (WhatsAppInteractiveButtonRequest, 
                                   InteractiveButton, 
                                   MessageBody, MessageHeader, 
                                   MessageFooter, ButtonAction,
                                   Button,ButtonReply,
                                   WhatsAppTextReplyRequest, TextBody
)

def build_aiml_program_payload(wa_id: str):
    """Builds the payload for the Computer Science -AI & ML program."""

    header = MessageHeader(
        text="💻Computer Science -AI & ML"
    )

    body = MessageBody(
        text=(
            "🎓 *B.Tech in Computer Science -AI & ML(AIML)*\n\n"
            "Learn core concepts in:\n"
            "• Programming\n"
            "• Software Development\n"
            "• Computer Networks\n"
            "• Database Management\n"
            "• Operating Systems\n"
            "• Web Technologies\n\n"
            "Get details about the program, fee structure, placements, "
            "and department information.\n\n"
            "Please choose an option below 👇"
        )
    )

    footer = MessageFooter(
        text="🎓 GM University Admissions 2026-27"
    )

    btn_program_details = Button(reply=ButtonReply(id="aaaca", title="Program Details"))
    btn_fee_duration = Button(reply=ButtonReply(id="aaacb", title="Fee & Duration"))
    btn_branch_website = Button(reply=ButtonReply(id="aaacc", title="Branch Website"))

    action = ButtonAction(buttons=[btn_program_details, btn_fee_duration, btn_branch_website])

    interactive = InteractiveButton(
        header=header,
        body=body,
        footer=footer,
        action=action,
    )

    payload = WhatsAppInteractiveButtonRequest(to=wa_id, interactive=interactive)
    return payload.model_dump()


def build_aiml_program_details_payload(wa_id: str):
    """Builds a well-formatted WhatsApp text payload for full AIML program details."""

    text = (
        "🎓 *B.Tech Computer Science -AI & ML (AIML)*\n"
        "📘 *Program Details – 2026-27 Intake*\n\n"

        "━━━━━━━━━━━━━━━\n"
        "📄 *Program Brochure Includes:*\n"
        "• Curriculum Structure\n"
        "• Eligibility Criteria\n"
        "• CSE Specializations\n"
        "• Department Highlights\n"
        "• Academic & Career Opportunities\n"
        "━━━━━━━━━━━━━━━\n\n"

        "🔗 *View Full Program Brochure:*\n"
        "https://gmu.ac.in/pdfview_assets%5Cdownloadmaterial%5CUG%20Programs%5Cprogram%5CPD_AIML_2026-27.pdf"
        
        "\n\n📞 *Contact Details*\n"
        "━━━━━━━━━━━━━━━\n"
        "📍 GM University, Davangere\n"
        "☎️ Phone: +91 9364099712,+91 9364099720\n"
        "📧 Email: hod.aiml@gmu.ac.in\n"
    )

    payload = WhatsAppTextReplyRequest(
        to=wa_id,
        text=TextBody(
            body=text,
            preview_url=True
        ),
    )

    return payload.model_dump()


def build_aiml_fee_duration_payload(wa_id: str):
    """Builds a well-formatted WhatsApp text payload for AIML fee and duration information."""

    text = (
        "🎓 *GM University – AIML Program Fee Details*\n\n"

        "⏱ *Duration:* 4 Years\n"
        "💻 *Current AIML Fee*\n"
        "━━━━━━━━━━━━━━━\n"
        "₹2,60,000 per year\n\n"
        
        "📞 *Contact Details*\n"
        "━━━━━━━━━━━━━━━\n"
        "📍 GM University, Davangere\n"
        "☎️ Phone: +91 9364099712,+91 9364099720\n"
        "📧 Email: hod.aiml@gmu.ac.in\n"
    )

    payload = WhatsAppTextReplyRequest(
        to=wa_id,
        text=TextBody(
            body=text,
            preview_url=True
        ),
    )

    return payload.model_dump()


def build_aiml_branch_website_payload(wa_id: str):
    """Builds a well-formatted WhatsApp text payload for the AIML branch website."""

    text = (
        "💻 *GM University – Computer Science -AI & ML*\n\n"

        "🌐 Explore the official AIML branch website for:\n"
        "━━━━━━━━━━━━━━━\n"
        "• Department Overview\n"
        "• Programs & Specializations\n"
        "• Faculty Information\n"
        "• Events & Activities\n"
        "• Placement Highlights\n"
        "• Student Resources\n"
        "━━━━━━━━━━━━━━━\n\n"

        "🔗 *Visit Website:*\n"
        "https://gmuaiml.netlify.app//"
    )

    payload = WhatsAppTextReplyRequest(
        to=wa_id,
        text=TextBody(
            body=text,
            preview_url=True
        ),
    )

    return payload.model_dump()
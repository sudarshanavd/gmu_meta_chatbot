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

def build_eee_program_payload(wa_id: str):
    """Builds the payload for the Electrical and Electronics Engineering program."""

    header = MessageHeader(
        text="⚡ Electrical and Electronics Engineering"
    )

    body = MessageBody(
        text=(
            "🎓 *B.Tech in Electrical and Electronics Engineering (EEE)*\n\n"
            "Learn core concepts in:\n"
            "• Electrical Circuits\n"
            "• Power Systems\n"
            "• Electrical Machines\n"
            "• Power Electronics\n"
            "• Control Systems\n"
            "• Renewable Energy Systems\n"
            "• High Voltage Engineering\n"
            "• Industrial Automation\n"
            "• Instrumentation & Measurement\n"
            "• Smart Grid Technologies\n\n"
            "Get details about the program, fee structure, placements, "
            "and department information.\n\n"
            "Please choose an option below 👇"
        )
    )

    footer = MessageFooter(
        text="🎓 GM University Admissions 2026-27"
    )

    btn_program_details = Button(reply=ButtonReply(id="aabba", title="Program Details"))
    btn_fee_duration = Button(reply=ButtonReply(id="aabbb", title="Fee & Duration"))
    btn_branch_website = Button(reply=ButtonReply(id="aabbc", title="Branch Website"))

    action = ButtonAction(buttons=[btn_program_details, btn_fee_duration, btn_branch_website])

    interactive = InteractiveButton(
        header=header,
        body=body,
        footer=footer,
        action=action,
    )

    payload = WhatsAppInteractiveButtonRequest(to=wa_id, interactive=interactive)
    return payload.model_dump()


def build_eee_program_details_payload(wa_id: str):
    """Builds a well-formatted WhatsApp text payload for full EEE program details."""

    text = (
        "🎓 *B.Tech Electrical and Electronics Engineering (EEE)*\n"
        "📘 *Program Details – 2026-27 Intake*\n\n"

        "━━━━━━━━━━━━━━━\n"
        "📄 *Program Brochure Includes:*\n"
        "• Curriculum Structure\n"
        "• Eligibility Criteria\n"
        "• Electrical & Electronics Core Subjects\n"
        "• Department Highlights\n"
        "• Academic & Career Opportunities\n"
        "━━━━━━━━━━━━━━━\n\n"

        "🔗 *View Full Program Brochure:*\n"
        "http://gmu.ac.in/pdfview_assets%5Cdownloadmaterial%5CUG%20Programs%5CPD_EEE_2026-27.pdf"
        "\n\n📞 *Contact Details*\n"
        "━━━━━━━━━━━━━━━\n"
        "📍 GM University, Davangere\n"
        "☎️ Phone: +91 9364099712,+91 9364099720\n"
        "📧 Email: hod.eee@gmu.ac.in\n"
    )

    payload = WhatsAppTextReplyRequest(
        to=wa_id,
        text=TextBody(
            body=text,
            preview_url=True
        ),
    )

    return payload.model_dump()


def build_eee_fee_duration_payload(wa_id: str):
    """Builds a well-formatted WhatsApp text payload for EEE fee and duration information."""

    text = (
        "🎓 *GM University – EEE Program Fee Details*\n\n"

        "⚡ *Current EEE Fee*\n"
        "━━━━━━━━━━━━━━━\n"
        "₹1,65,000 per year\n\n"
        
        "⏳ *Program Duration*\n"
        "━━━━━━━━━━━━━━━\n"
        "4 Years (8 Semesters)\n\n"

        "📞 *Contact Details*\n"
        "━━━━━━━━━━━━━━━\n"
        "📍 GM University, Davangere\n"
        "☎️ Phone: +91 9364099712,+91 9364099720\n"
        "📧 Email: hod.eee@gmu.ac.in\n"
    )

    payload = WhatsAppTextReplyRequest(
        to=wa_id,
        text=TextBody(
            body=text,
            preview_url=True
        ),
    )

    return payload.model_dump()


def build_eee_branch_website_payload(wa_id: str):
    """Builds a well-formatted WhatsApp text payload for the EEE branch website."""

    text = (
        "⚡ *GM University – Electrical and Electronics Engineering*\n\n"

        "🌐 Explore the official EEE branch website for:\n"
        "━━━━━━━━━━━━━━━\n"
        "• Department Overview\n"
        "• Programs & Curriculum\n"
        "• Faculty Information\n"
        "• Electrical Machines Lab\n"
        "• Power Systems & Electronics Lab\n"
        "• Events & Activities\n"
        "• Placement Highlights\n"
        "• Student Resources\n"
        "━━━━━━━━━━━━━━━\n\n"

        "🔗 *Visit Website:*\n"
        "https://gmu.ac.in/EEE/"
    )

    payload = WhatsAppTextReplyRequest(
        to=wa_id,
        text=TextBody(
            body=text,
            preview_url=True
        ),
    )

    return payload.model_dump()
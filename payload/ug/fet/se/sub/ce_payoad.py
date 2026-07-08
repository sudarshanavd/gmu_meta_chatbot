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

def build_ce_program_payload(wa_id: str):
    """Builds the payload for the Civil Engineering program."""

    header = MessageHeader(
        text="🏗️ Civil Engineering"
    )

    body = MessageBody(
        text=(
            "🎓 *B.Tech in Civil Engineering (CE)*\n\n"
            "Learn core concepts in:\n"
            "• Structural Engineering\n"
            "• Construction Technology\n"
            "• Surveying & Geomatics\n"
            "• Geotechnical Engineering\n"
            "• Transportation Engineering\n"
            "• Environmental Engineering\n"
            "• Water Resources Engineering\n"
            "• Concrete Technology\n"
            "• Urban Planning\n"
            "• Project Management\n\n"
            "Get details about the program, fee structure, placements, "
            "and department information.\n\n"
            "Please choose an option below 👇"
        )
    )

    footer = MessageFooter(
        text="🎓 GM University Admissions 2026-27"
    )

    btn_program_details = Button(reply=ButtonReply(id="aabea", title="Program Details"))
    btn_fee_duration = Button(reply=ButtonReply(id="aabeb", title="Fee & Duration"))
    btn_branch_website = Button(reply=ButtonReply(id="aabec", title="Branch Website"))

    action = ButtonAction(buttons=[btn_program_details, btn_fee_duration, btn_branch_website])

    interactive = InteractiveButton(
        header=header,
        body=body,
        footer=footer,
        action=action,
    )

    payload = WhatsAppInteractiveButtonRequest(to=wa_id, interactive=interactive)
    return payload.model_dump()


def build_ce_program_details_payload(wa_id: str):
    """Builds a well-formatted WhatsApp text payload for full Civil Engineering program details."""

    text = (
        "🎓 *B.Tech Civil Engineering (CE)*\n"
        "📘 *Program Details – 2026-27 Intake*\n\n"

        "━━━━━━━━━━━━━━━\n"
        "📄 *Program Brochure Includes:*\n"
        "• Curriculum Structure\n"
        "• Eligibility Criteria\n"
        "• Civil Engineering Core Subjects\n"
        "• Department Highlights\n"
        "• Academic & Career Opportunities\n"
        "━━━━━━━━━━━━━━━\n\n"

        "🔗 *View Full Program Brochure:*\n"
        "https://gmu.ac.in/pdfview_assets%5Cdownloadmaterial%5CUG%20Programs%5CPD_CE_2026-27.pdf"

        "\n\n📞 *Contact Details*\n"
        "━━━━━━━━━━━━━━━\n"
        "📍 GM University, Davangere\n"
        "☎️ Phone: +91 9364099712,+91 9364099720\n"
        "📧 Email: hod.ce@gmu.ac.in\n"
    )

    payload = WhatsAppTextReplyRequest(
        to=wa_id,
        text=TextBody(
            body=text,
            preview_url=True
        ),
    )

    return payload.model_dump()


def build_ce_fee_duration_payload(wa_id: str):
    """Builds a well-formatted WhatsApp text payload for Civil Engineering fee and duration information."""

    text = (
        "🎓 *GM University – Civil Engineering Program Fee Details*\n\n"

        "🏗️ *Current Civil Engineering Fee*\n"
        "━━━━━━━━━━━━━━━\n"
        "₹1,65,000 per year\n\n"
        
        "⏳ *Program Duration*\n"
        "━━━━━━━━━━━━━━━\n"
        "4 Years (8 Semesters)\n\n"

        "📞 *Contact Details*\n"
        "━━━━━━━━━━━━━━━\n"
        "📍 GM University, Davangere\n"
        "☎️ Phone: +91 9364099712,+91 9364099720\n"
        "📧 Email: hod.ce@gmu.ac.in\n"
    )

    payload = WhatsAppTextReplyRequest(
        to=wa_id,
        text=TextBody(
            body=text,
            preview_url=True
        ),
    )

    return payload.model_dump()


def build_ce_branch_website_payload(wa_id: str):
    """Builds a well-formatted WhatsApp text payload for the Civil Engineering branch website."""

    text = (
        "🏗️ *GM University – Civil Engineering*\n\n"

        "🌐 Explore the official Civil Engineering website for:\n"
        "━━━━━━━━━━━━━━━\n"
        "• Department Overview\n"
        "• Programs & Curriculum\n"
        "• Faculty Information\n"
        "• Surveying & Geotechnical Labs\n"
        "• Structures & Construction Labs\n"
        "• Events & Activities\n"
        "• Placement Highlights\n"
        "• Student Resources\n"
        "━━━━━━━━━━━━━━━\n\n"

        "🔗 *Visit Website:*\n"
        "https://civil-dept.netlify.app/"
    )

    payload = WhatsAppTextReplyRequest(
        to=wa_id,
        text=TextBody(
            body=text,
            preview_url=True
        ),
    )

    return payload.model_dump()
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

def build_ece_program_payload(wa_id: str):
    """Builds the payload for the Electronics and Communication Engineering program."""

    header = MessageHeader(
        text="📡 Electronics and Communication Engineering"
    )

    body = MessageBody(
        text=(
            "🎓 *B.Tech in Electronics and Communication Engineering (ECE)*\n\n"
            "Learn core concepts in:\n"
            "• Electronic Circuits\n"
            "• Analog & Digital Communication\n"
            "• Microprocessors & Microcontrollers\n"
            "• VLSI Design\n"
            "• Embedded Systems\n"
            "• Signal Processing\n"
            "• Control Systems\n"
            "• Wireless Communication\n"
            "• Internet of Things (IoT)\n"
            "• Robotics & Automation\n\n"
            "Get details about the program, fee structure, placements, "
            "and department information.\n\n"
            "Please choose an option below 👇"
        )
    )

    footer = MessageFooter(
        text="🎓 GM University Admissions 2026-27"
    )

    btn_program_details = Button(reply=ButtonReply(id="aabaa", title="Program Details"))
    btn_fee_duration = Button(reply=ButtonReply(id="aabab", title="Fee & Duration"))
    btn_branch_website = Button(reply=ButtonReply(id="aabac", title="Branch Website"))

    action = ButtonAction(buttons=[btn_program_details, btn_fee_duration, btn_branch_website])

    interactive = InteractiveButton(
        header=header,
        body=body,
        footer=footer,
        action=action,
    )

    payload = WhatsAppInteractiveButtonRequest(to=wa_id, interactive=interactive)
    return payload.model_dump()


def build_ece_program_details_payload(wa_id: str):
    """Builds a well-formatted WhatsApp text payload for full ECE program details."""

    text = (
        "🎓 *B.Tech Electronics and Communication Engineering (ECE)*\n"
        "📘 *Program Details – 2026-27 Intake*\n\n"

        "━━━━━━━━━━━━━━━\n"
        "📄 *Program Brochure Includes:*\n"
        "• Curriculum Structure\n"
        "• Eligibility Criteria\n"
        "• Electronics & Communication Core Subjects\n"
        "• Department Highlights\n"
        "• Academic & Career Opportunities\n"
        "━━━━━━━━━━━━━━━\n\n"

        "🔗 *View Full Program Brochure:*\n"
        "https://gmu.ac.in/pdfview_assets%5Cdownloadmaterial%5CUG%20Programs%5CPD_ECE_2026-27.pdf"
        "\n\n📞 *Contact Details*\n"
        "━━━━━━━━━━━━━━━\n"
        "📍 GM University, Davangere\n"
        "☎️ Phone: +91 9364099712,+91 9364099720\n"
        "📧 Email: hod.ece@gmu.ac.in\n"
    )

    payload = WhatsAppTextReplyRequest(
        to=wa_id,
        text=TextBody(
            body=text,
            preview_url=True
        ),
    )

    return payload.model_dump()


def build_ece_fee_duration_payload(wa_id: str):
    """Builds a well-formatted WhatsApp text payload for ECE fee and duration information."""

    text = (
        "🎓 *GM University – ECE Program Fee Details*\n\n"

        "📡 *Current ECE Fee*\n"
        "━━━━━━━━━━━━━━━\n"
        "₹2,10,000 per year\n\n"

        "⏳ *Program Duration*\n"
        "━━━━━━━━━━━━━━━\n"
        "4 Years (8 Semesters)\n\n"

        "📞 *Contact Details*\n"
        "━━━━━━━━━━━━━━━\n"
        "📍 GM University, Davangere\n"
        "☎️ Phone: +91 9364099712,+91 9364099720\n"
        "📧 Email: hod.ece@gmu.ac.in\n"
    )

    payload = WhatsAppTextReplyRequest(
        to=wa_id,
        text=TextBody(
            body=text,
            preview_url=True
        ),
    )

    return payload.model_dump()


def build_ece_branch_website_payload(wa_id: str):
    """Builds a well-formatted WhatsApp text payload for the ECE branch website."""

    text = (
        "📡 *GM University – Electronics and Communication Engineering*\n\n"

        "🌐 Explore the official ECE branch website for:\n"
        "━━━━━━━━━━━━━━━\n"
        "• Department Overview\n"
        "• Programs & Curriculum\n"
        "• Faculty Information\n"
        "• Laboratories & Facilities\n"
        "• Events & Activities\n"
        "• Placement Highlights\n"
        "• Student Resources\n"
        "━━━━━━━━━━━━━━━\n\n"

        "🔗 *Visit Website:*\n"
        "https://gmu.ac.in/ece/"
    )

    payload = WhatsAppTextReplyRequest(
        to=wa_id,
        text=TextBody(
            body=text,
            preview_url=True
        ),
    )

    return payload.model_dump()
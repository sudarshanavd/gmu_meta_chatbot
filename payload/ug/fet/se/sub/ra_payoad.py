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

def build_ra_program_payload(wa_id: str):
    """Builds the payload for the Robotics and Automation program."""

    header = MessageHeader(
        text="🤖 Robotics and Automation"
    )

    body = MessageBody(
        text=(
            "🎓 *B.Tech in Robotics and Automation (RA)*\n\n"
            "Learn core concepts in:\n"
            "• Robotics Engineering\n"
            "• Industrial Automation\n"
            "• Artificial Intelligence\n"
            "• Machine Learning\n"
            "• Embedded Systems\n"
            "• Mechatronics\n"
            "• Control Systems\n"
            "• Computer Vision\n"
            "• Autonomous Systems\n"
            "• Internet of Things (IoT)\n\n"
            "Get details about the program, fee structure, placements, "
            "and department information.\n\n"
            "Please choose an option below 👇"
        )
    )

    footer = MessageFooter(
        text="🎓 GM University Admissions 2026-27"
    )

    btn_program_details = Button(reply=ButtonReply(id="aabca", title="Program Details"))
    btn_fee_duration = Button(reply=ButtonReply(id="aabcb", title="Fee & Duration"))
    btn_branch_website = Button(reply=ButtonReply(id="aabcc", title="Branch Website"))

    action = ButtonAction(buttons=[btn_program_details, btn_fee_duration, btn_branch_website])

    interactive = InteractiveButton(
        header=header,
        body=body,
        footer=footer,
        action=action,
    )

    payload = WhatsAppInteractiveButtonRequest(to=wa_id, interactive=interactive)
    return payload.model_dump()


def build_ra_program_details_payload(wa_id: str):
    """Builds a well-formatted WhatsApp text payload for full Robotics and Automation program details."""

    text = (
        "🎓 *B.Tech Robotics and Automation (RA)*\n"
        "📘 *Program Details – 2026-27 Intake*\n\n"

        "━━━━━━━━━━━━━━━\n"
        "📄 *Program Brochure Includes:*\n"
        "• Curriculum Structure\n"
        "• Eligibility Criteria\n"
        "• Robotics & Automation Core Subjects\n"
        "• Department Highlights\n"
        "• Academic & Career Opportunities\n"
        "━━━━━━━━━━━━━━━\n\n"

        "🔗 *View Full Program Brochure:*\n"
        "https://gmu.ac.in/pdfview_assets%5Cdownloadmaterial%5CUG%20Programs%5CPD_RA_2026-27.pdf"
        "\n\n📞 *Contact Details*\n"
        "━━━━━━━━━━━━━━━\n"
        "📍 GM University, Davangere\n"
        "☎️ Phone: +91 9364099712,+91 9364099720\n"
        "📧 Email:  hod.ra@gmu.ac.in\n"
    )

    payload = WhatsAppTextReplyRequest(
        to=wa_id,
        text=TextBody(
            body=text,
            preview_url=True
        ),
    )

    return payload.model_dump()


def build_ra_fee_duration_payload(wa_id: str):
    """Builds a well-formatted WhatsApp text payload for Robotics and Automation fee and duration information."""

    text = (
        "🎓 *GM University – Robotics and Automation Program Fee Details*\n\n"

        "🤖 *Current Robotics and Automation Fee*\n"
        "━━━━━━━━━━━━━━━\n"
        "₹1,65,000 per year\n\n"

        "⏳ *Program Duration*\n"
        "━━━━━━━━━━━━━━━\n"
        "4 Years (8 Semesters)\n\n"

        "📞 *Contact Details*\n"
        "━━━━━━━━━━━━━━━\n"
        "📍 GM University, Davangere\n"
        "☎️ Phone: +91 9364099712,+91 9364099720\n"
        "📧 Email:  hod.ra@gmu.ac.in\n"
    )

    payload = WhatsAppTextReplyRequest(
        to=wa_id,
        text=TextBody(
            body=text,
            preview_url=True
        ),
    )

    return payload.model_dump()


def build_ra_branch_website_payload(wa_id: str):
    """Builds a well-formatted WhatsApp text payload for the Robotics and Automation branch website."""

    text = (
        "🤖 *GM University – Robotics and Automation*\n\n"

        "🌐 Explore the official RA branch website for:\n"
        "━━━━━━━━━━━━━━━\n"
        "• Department Overview\n"
        "• Programs & Curriculum\n"
        "• Faculty Information\n"
        "• Robotics & Automation Labs\n"
        "• Events & Activities\n"
        "• Placement Highlights\n"
        "• Student Resources\n"
        "━━━━━━━━━━━━━━━\n\n"

        "🔗 *Visit Website:*\n"
        "https://ra-gmu.netlify.app/"
    )

    payload = WhatsAppTextReplyRequest(
        to=wa_id,
        text=TextBody(
            body=text,
            preview_url=True
        ),
    )

    return payload.model_dump()
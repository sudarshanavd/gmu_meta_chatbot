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

def build_iy_program_payload(wa_id: str):
    """Builds the payload for the Computer Science - Information Security program."""

    header = MessageHeader(
        text="🔐 Computer Science - Information Security"
    )

    body = MessageBody(
        text=(
            "🎓 *B.Tech in Computer Science - Information Security (CS-IY)*\n\n"
            "Learn core concepts in:\n"
            "• Information Security\n"
            "• Cyber Security\n"
            "• Ethical Hacking\n"
            "• Network Security\n"
            "• Cryptography\n"
            "• Digital Forensics\n"
            "• Secure Software Development\n"
            "• Cloud Security\n"
            "• Malware Analysis\n"
            "• Incident Response & Risk Management\n\n"
            "Get details about the program, fee structure, placements, "
            "and department information.\n\n"
            "Please choose an option below 👇"
        )
    )

    footer = MessageFooter(
        text="🎓 GM University Admissions 2026-27"
    )

    btn_program_details = Button(reply=ButtonReply(id="aaaia", title="Program Details"))
    btn_fee_duration = Button(reply=ButtonReply(id="aaajb", title="Fee & Duration"))
    btn_branch_website = Button(reply=ButtonReply(id="aaajc", title="Branch Website"))

    action = ButtonAction(buttons=[btn_program_details, btn_fee_duration, btn_branch_website])

    interactive = InteractiveButton(
        header=header,
        body=body,
        footer=footer,
        action=action,
    )

    payload = WhatsAppInteractiveButtonRequest(to=wa_id, interactive=interactive)
    return payload.model_dump()


def build_iy_program_details_payload(wa_id: str):
    """Builds a well-formatted WhatsApp text payload for full Information Security program details."""

    text = (
        "🎓 *B.Tech Computer Science - Information Security (CS-IY)*\n"
        "📘 *Program Details – 2026-27 Intake*\n\n"

        "━━━━━━━━━━━━━━━\n"
        "📄 *Program Brochure Includes:*\n"
        "• Curriculum Structure\n"
        "• Eligibility Criteria\n"
        "• Information Security Core Subjects\n"
        "• Department Highlights\n"
        "• Academic & Career Opportunities\n"
        "━━━━━━━━━━━━━━━\n\n"

        "🔗 *View Full Program Brochure:*\n"
        "https://gmu.ac.in/pdfview_assets%5Cdownloadmaterial%5CUG%20Programs%5Cprogram%5CPD_CC_2026-27.pdf"
        "\n\n📞 *Contact Details*\n"
        "━━━━━━━━━━━━━━━\n"
        "📍 GM University, Davangere\n"
        "☎️ Phone: +91 9364099712,+91 9364099720\n"
        "📧 Email: hod.cyiy@gmu.ac.in\n"
    )

    payload = WhatsAppTextReplyRequest(
        to=wa_id,
        text=TextBody(
            body=text,
            preview_url=True
        ),
    )

    return payload.model_dump()


def build_iy_fee_duration_payload(wa_id: str):
    """Builds a well-formatted WhatsApp text payload for Information Security fee and duration information."""

    text = (
        "🎓 *GM University – Information Security Program Fee Details*\n\n"

        "⏱ *Duration:* 4 Years\n"
        "🔐 *Current Information Security Fee*\n"
        "━━━━━━━━━━━━━━━\n"
        "₹2,25,000 per year\n\n"

        "📞 *Contact Details*\n"
        "━━━━━━━━━━━━━━━\n"
        "📍 GM University, Davangere\n"
        "☎️ Phone: +91 9364099712,+91 9364099720\n"
        "📧 Email: hod.cyiy@gmu.ac.in\n"
    )

    payload = WhatsAppTextReplyRequest(
        to=wa_id,
        text=TextBody(
            body=text,
            preview_url=True
        ),
    )

    return payload.model_dump()


def build_iy_branch_website_payload(wa_id: str):
    """Builds a well-formatted WhatsApp text payload for the Information Security branch website."""

    text = (
        "🔐 *GM University – Computer Science - Information Security*\n\n"

        "🌐 Explore the official Information Security branch website for:\n"
        "━━━━━━━━━━━━━━━\n"
        "• Department Overview\n"
        "• Programs & Curriculum\n"
        "• Faculty Information\n"
        "• Security Labs & Facilities\n"
        "• Events & Activities\n"
        "• Placement Highlights\n"
        "• Student Resources\n"
        "━━━━━━━━━━━━━━━\n\n"

        "🔗 *Visit Website:*\n"
        "https://gmu.ac.in/cc-bs/"
    )

    payload = WhatsAppTextReplyRequest(
        to=wa_id,
        text=TextBody(
            body=text,
            preview_url=True
        ),
    )

    return payload.model_dump()
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

def build_cc_program_payload(wa_id: str):
    """Builds the payload for the Computer Science - Cloud Computing program."""

    header = MessageHeader(
        text="☁️ Computer Science - Cloud Computing"
    )

    body = MessageBody(
        text=(
            "🎓 *B.Tech in Computer Science - Cloud Computing (CS-CC)*\n\n"
            "Learn core concepts in:\n"
            "• Cloud Computing\n"
            "• Virtualization Technologies\n"
            "• Distributed Systems\n"
            "• Computer Networks\n"
            "• Database Management Systems\n"
            "• DevOps & Automation\n"
            "• Cyber Security\n"
            "• Containerization & Kubernetes\n"
            "• Big Data Analytics\n"
            "• Web & Enterprise Applications\n\n"
            "Get details about the program, fee structure, placements, "
            "and department information.\n\n"
            "Please choose an option below 👇"
        )
    )

    footer = MessageFooter(
        text="🎓 GM University Admissions 2026-27"
    )

    btn_program_details = Button(reply=ButtonReply(id="aaaha", title="Program Details"))
    btn_fee_duration = Button(reply=ButtonReply(id="aaahb", title="Fee & Duration"))
    btn_branch_website = Button(reply=ButtonReply(id="aaahc", title="Branch Website"))

    action = ButtonAction(buttons=[btn_program_details, btn_fee_duration, btn_branch_website])

    interactive = InteractiveButton(
        header=header,
        body=body,
        footer=footer,
        action=action,
    )

    payload = WhatsAppInteractiveButtonRequest(to=wa_id, interactive=interactive)
    return payload.model_dump()


def build_cc_program_details_payload(wa_id: str):
    """Builds a well-formatted WhatsApp text payload for full Cloud Computing program details."""

    text = (
        "🎓 *B.Tech Computer Science - Cloud Computing (CS-CC)*\n"
        "📘 *Program Details – 2026-27 Intake*\n\n"

        "━━━━━━━━━━━━━━━\n"
        "📄 *Program Brochure Includes:*\n"
        "• Curriculum Structure\n"
        "• Eligibility Criteria\n"
        "• Cloud Computing Core Subjects\n"
        "• Department Highlights\n"
        "• Academic & Career Opportunities\n"
        "━━━━━━━━━━━━━━━\n\n"

        "🔗 *View Full Program Brochure:*\n"
        "https://gmu.ac.in/pdfview_assets%5Cdownloadmaterial%5CUG%20Programs%5Cprogram%5CPD_CC_2026-27.pdf"
        "\n\n📞 *Contact Details*\n"
        "━━━━━━━━━━━━━━━\n"
        "📍 GM University, Davangere\n"
        "☎️ Phone: +91 9364099712,+91 9364099720\n"
        "📧 Email: hod.bcbs@gmu.ac.in\n"
    )

    payload = WhatsAppTextReplyRequest(
        to=wa_id,
        text=TextBody(
            body=text,
            preview_url=True
        ),
    )

    return payload.model_dump()


def build_cc_fee_duration_payload(wa_id: str):
    """Builds a well-formatted WhatsApp text payload for Cloud Computing fee and duration information."""

    text = (
        "🎓 *GM University – Cloud Computing Program Fee Details*\n\n"

        "⏱ *Duration:* 4 Years\n"
        "☁️ *Current Cloud Computing Fee*\n"
        "━━━━━━━━━━━━━━━\n"
        "₹2,25,000 per year\n\n"

        "📞 *Contact Details*\n"
        "━━━━━━━━━━━━━━━\n"
        "📍 GM University, Davangere\n"
        "☎️ Phone: +91 9364099712,+91 9364099720\n"
        "📧 Email: hod.bcbs@gmu.ac.in\n"
    )

    payload = WhatsAppTextReplyRequest(
        to=wa_id,
        text=TextBody(
            body=text,
            preview_url=True
        ),
    )

    return payload.model_dump()


def build_cc_branch_website_payload(wa_id: str):
    """Builds a well-formatted WhatsApp text payload for the Cloud Computing branch website."""

    text = (
        "☁️ *GM University – Computer Science - Cloud Computing*\n\n"

        "🌐 Explore the official Cloud Computing branch website for:\n"
        "━━━━━━━━━━━━━━━\n"
        "• Department Overview\n"
        "• Programs & Curriculum\n"
        "• Faculty Information\n"
        "• Cloud Labs & Facilities\n"
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
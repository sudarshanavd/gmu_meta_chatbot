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


def build_mba_professional_program_payload(wa_id: str):
    """Builds the payload for the MBA Professional program."""

    header = MessageHeader(text="🏆📈 MBA Professional")

    body = MessageBody(
        text=(
            "🎓 *MBA Professional*\n\n"
            "Learn core concepts in:\n"
            "• Strategic Management\n"
            "• Leadership and Decision Making\n"
            "• Financial Management\n"
            "• Marketing Management\n"
            "• Human Resource Management\n"
            "• Business Analytics\n"
            "• Operations and Supply Chain Management\n"
            "• Entrepreneurship and Innovation\n"
            "• Corporate Governance\n"
            "• Digital Business Transformation\n\n"
            "Get details about the program, eligibility, curriculum, "
            "industry exposure, professional development, and career opportunities.\n\n"
            "Please choose an option below 👇"
        )
    )

    footer = MessageFooter(text="🎓 GM University Admissions 2026-27")

    btn_program_details = Button(reply=ButtonReply(id="beaba", title="Program Details"))
    btn_fee_duration = Button(reply=ButtonReply(id="beabb", title="Fee Details"))
    btn_branch_website = Button(reply=ButtonReply(id="beabc", title="More Info"))

    action = ButtonAction(buttons=[btn_program_details, btn_fee_duration, btn_branch_website])

    interactive = InteractiveButton(
        header=header,
        body=body,
        footer=footer,
        action=action,
    )

    payload = WhatsAppInteractiveButtonRequest(to=wa_id, interactive=interactive)
    return payload.model_dump()


def build_mba_professional_program_details_payload(wa_id: str):
    """Builds a WhatsApp text payload for MBA Professional program details."""

    text = (
        "🎓 *MBA Professional*\n"
        "📘 *Program Details – 2026-27 Intake*\n\n"
        "━━━━━━━━━━━━━━━\n"
        "📄 *Program Details Include:*\n"
        "• Curriculum Structure\n"
        "• Eligibility Criteria\n"
        "• Advanced Management Subjects\n"
        "• Leadership and Business Strategy Concepts\n"
        "• Industry-Oriented Learning\n"
        "• Practical & Project-Based Training\n"
        "• Career Opportunities\n"
        "━━━━━━━━━━━━━━━\n\n"
        "📞 *Contact Details*\n"
        "━━━━━━━━━━━━━━━\n"
        "📍 GM University, Davangere\n"
        "☎️ Phone: +91 9364099712,+91 9364099720\n"
        # "📧 Email: info@gmu.ac.in\n"
    )

    payload = WhatsAppTextReplyRequest(
        to=wa_id,
        text=TextBody(body=text, preview_url=False),
    )

    return payload.model_dump()


def build_mba_professional_fee_duration_payload(wa_id: str):
    """Builds a WhatsApp text payload for MBA Professional fee information."""

    text = (
        "🎓 *GM University – MBA Professional Fee Details*\n\n"
        "⏱ *Duration:* 2 Years\n"
        "💰 *Program Annual Fee:* ₹3,15,000\n\n"
        "📘 *Program Information:*\n"
        "━━━━━━━━━━━━━━━\n"
        "• Premium industry-focused management postgraduate program\n"
        "• Strong foundation in leadership, strategy and business management\n"
        "• Advanced industry exposure and professional development\n"
        "• Corporate-oriented practical training and internships\n"
        "• Career opportunities in consulting, leadership roles, business management, entrepreneurship and global organizations\n"
        "━━━━━━━━━━━━━━━"
    )

    payload = WhatsAppTextReplyRequest(
        to=wa_id,
        text=TextBody(body=text, preview_url=False),
    )

    return payload.model_dump()


def build_mba_professional_branch_website_payload(wa_id: str):
    """Builds a WhatsApp text payload for MBA Professional information."""

    text = (
        "🏆📈 *GM University – MBA Professional*\n\n"
        "📌 Official program link will be updated soon.\n\n"
        "Stay connected with GM University for updates regarding:\n"
        "━━━━━━━━━━━━━━━\n"
        "• Program Overview\n"
        "• Curriculum Details\n"
        "• Industry Training\n"
        "• Leadership Development\n"
        "• Corporate Projects\n"
        "• Placement Opportunities\n"
        "• Student Resources\n"
        "━━━━━━━━━━━━━━━"
    )

    payload = WhatsAppTextReplyRequest(
        to=wa_id,
        text=TextBody(body=text, preview_url=False),
    )

    return payload.model_dump()

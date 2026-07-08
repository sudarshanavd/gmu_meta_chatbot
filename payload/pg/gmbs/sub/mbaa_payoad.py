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

def build_mba_advanced_program_payload(wa_id: str):
    """Builds the payload for the MBA Advanced program."""

    header = MessageHeader(text="🚀📈 MBA Advanced")

    body = MessageBody(
        text=(
            "🎓 *MBA Advanced*\n\n"
            "Learn core concepts in:\n"
            "• Advanced Strategic Management\n"
            "• Global Business Leadership\n"
            "• Financial Analytics\n"
            "• Marketing Strategy\n"
            "• Human Capital Management\n"
            "• Business Intelligence and Analytics\n"
            "• Operations Excellence\n"
            "• Innovation and Entrepreneurship\n"
            "• Corporate Governance and Ethics\n"
            "• Digital Transformation and Emerging Technologies\n\n"
            "Get details about the program, eligibility, curriculum, "
            "global industry exposure, executive learning, and career opportunities.\n\n"
            "Please choose an option below 👇"
        )
    )

    footer = MessageFooter(text="🎓 GM University Admissions 2026-27")

    action = ButtonAction(
        buttons=[
            Button(reply=ButtonReply(id="beaca", title="Program Details")),
            Button(reply=ButtonReply(id="beacb", title="Fee Details")),
            Button(reply=ButtonReply(id="beacc", title="More Info")),
        ]
    )

    interactive = InteractiveButton(
        header=header,
        body=body,
        footer=footer,
        action=action,
    )

    payload = WhatsAppInteractiveButtonRequest(
        to=wa_id,
        interactive=interactive
    )

    return payload.model_dump()


def build_mba_advanced_program_details_payload(wa_id: str):
    """Builds a WhatsApp text payload for MBA Advanced program details."""

    text = (
        "🎓 *MBA Advanced*\n"
        "📘 *Program Details – 2026-27 Intake*\n\n"
        "━━━━━━━━━━━━━━━\n"
        "📄 *Program Details Include:*\n"
        "• Curriculum Structure\n"
        "• Eligibility Criteria\n"
        "• Advanced Management Subjects\n"
        "• Global Leadership and Strategy Concepts\n"
        "• Industry-Oriented Learning\n"
        "• Executive & Project-Based Training\n"
        "• Career Opportunities\n"
        "━━━━━━━━━━━━━━━\n\n"
        "📞 *Contact Details*\n"
        "━━━━━━━━━━━━━━━\n"
        "📍 GM University, Davangere\n"
        "☎️ Phone: +91 9364099712,+91 9364099720\n"
        "📧 Email: info@gmu.ac.in"
    )

    payload = WhatsAppTextReplyRequest(
        to=wa_id,
        text=TextBody(body=text, preview_url=False),
    )

    return payload.model_dump()


def build_mba_advanced_fee_duration_payload(wa_id: str):
    """Builds a WhatsApp text payload for MBA Advanced fee information."""

    text = (
        "🎓 *GM University – MBA Advanced Fee Details*\n\n"
        "⏱ *Duration:* 2 Years\n"
        "💰 *Program Annual Fee:* ₹4,15,000\n\n"
        "📘 *Program Information:*\n"
        "━━━━━━━━━━━━━━━\n"
        "• Premium advanced management postgraduate program\n"
        "• Strong foundation in leadership, global business and strategic decision-making\n"
        "• Advanced industry exposure and executive learning\n"
        "• Corporate-focused practical training and internships\n"
        "• Career opportunities in consulting, senior management, entrepreneurship, business leadership and multinational organizations\n"
        "━━━━━━━━━━━━━━━"
    )

    payload = WhatsAppTextReplyRequest(
        to=wa_id,
        text=TextBody(body=text, preview_url=False),
    )

    return payload.model_dump()


def build_mba_advanced_branch_website_payload(wa_id: str):
    """Builds a WhatsApp text payload for MBA Advanced information."""

    text = (
        "🚀📈 *GM University – MBA Advanced*\n\n"
        "📌 Official program link will be updated soon.\n\n"
        "Stay connected with GM University for updates regarding:\n"
        "━━━━━━━━━━━━━━━\n"
        "• Program Overview\n"
        "• Curriculum Details\n"
        "• Executive Training\n"
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



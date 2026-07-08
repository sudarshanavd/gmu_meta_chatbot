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


def build_mba_program_payload(wa_id: str):
    """Builds the payload for the MBA program."""

    header = MessageHeader(
        text="📈🎓 Master of Business Administration (MBA)"
    )

    body = MessageBody(
        text=(
            "🎓 *Master of Business Administration (MBA)*\n\n"
            "Learn core concepts in:\n"
            "• Marketing Management\n"
            "• Financial Management\n"
            "• Human Resource Management\n"
            "• Operations Management\n"
            "• Business Analytics\n"
            "• Strategic Management\n"
            "• Entrepreneurship\n"
            "• Organizational Behaviour\n"
            "• Digital Business\n"
            "• Leadership and Innovation\n\n"
            "Get details about the program, eligibility, curriculum, "
            "practical learning, industry exposure, and career opportunities.\n\n"
            "Please choose an option below 👇"
        )
    )

    footer = MessageFooter(
        text="🎓 GM University Admissions 2026-27"
    )

    btn_program_details = Button(reply=ButtonReply(id="beaaa", title="Program Details"))
    btn_fee_duration = Button(reply=ButtonReply(id="beaab", title="Fee Details"))
    btn_branch_website = Button(reply=ButtonReply(id="beaac", title="More Info"))

    action = ButtonAction(buttons=[btn_program_details, btn_fee_duration, btn_branch_website])

    interactive = InteractiveButton(
        header=header,
        body=body,
        footer=footer,
        action=action,
    )

    payload = WhatsAppInteractiveButtonRequest(to=wa_id, interactive=interactive)
    return payload.model_dump()


def build_mba_program_details_payload(wa_id: str):
    """Builds a WhatsApp text payload for MBA program details."""

    text = (
        "🎓 *Master of Business Administration (MBA)*\n"
        "📘 *Program Details – 2026-27 Intake*\n\n"

        "━━━━━━━━━━━━━━━\n"
        "📄 *Program Details Include:*\n"
        "• Curriculum Structure\n"
        "• Eligibility Criteria\n"
        "• Management Core Subjects\n"
        "• Leadership and Strategic Management Concepts\n"
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
        text=TextBody(
            body=text,
            preview_url=False
        ),
    )

    return payload.model_dump()


def build_mba_fee_duration_payload(wa_id: str):
    """Builds a WhatsApp text payload for MBA fee information."""

    text = (
        "🎓 *GM University – MBA Fee Details*\n\n"

        "⏱ *Duration:* 2 Years\n"
        "💰 *Program Annual Fee:* ₹1,80,000\n\n"

        "📘 *Program Information:*\n"
        "━━━━━━━━━━━━━━━\n"
        "• Industry-focused management postgraduate program\n"
        "• Strong foundation in marketing, finance, HR and operations\n"
        "• Leadership, innovation and business strategy learning\n"
        "• Industry-oriented practical training and internships\n"
        "• Career opportunities in management, consulting, banking, marketing, HR and entrepreneurship\n"
        "━━━━━━━━━━━━━━━"
    )

    payload = WhatsAppTextReplyRequest(
        to=wa_id,
        text=TextBody(
            body=text,
            preview_url=False
        ),
    )

    return payload.model_dump()


def build_mba_branch_website_payload(wa_id: str):
    """Builds a WhatsApp text payload for MBA information."""

    text = (
        "📈🎓 *GM University – Master of Business Administration (MBA)*\n\n"

        "📌 Official program link will be updated soon.\n\n"

        "Stay connected with GM University for updates regarding:\n"
        "━━━━━━━━━━━━━━━\n"
        "• Program Overview\n"
        "• Curriculum Details\n"
        "• Industry Training\n"
        "• Management Projects\n"
        "• Placement Opportunities\n"
        "• Admission Information\n"
        "• Student Resources\n"
        "━━━━━━━━━━━━━━━"
    )

    payload = WhatsAppTextReplyRequest(
        to=wa_id,
        text=TextBody(
            body=text,
            preview_url=False
        ),
    )

    return payload.model_dump()
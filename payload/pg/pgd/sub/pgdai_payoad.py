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

def build_pgd_ai_iot_program_payload(wa_id: str):
    """Builds the payload for the PGD in AI and IoT with Intel program."""

    header = MessageHeader(
        text="🤖🌐 PGD in AI & IoT with Intel"
    )

    body = MessageBody(
        text=(
            "🎓 *PGD in AI & IoT with Intel*\n\n"
            "Learn core concepts in:\n"
            "• Artificial Intelligence Fundamentals\n"
            "• Machine Learning\n"
            "• Internet of Things (IoT)\n"
            "• Intelligent Systems Design\n"
            "• Embedded Systems\n"
            "• Sensor Networks\n"
            "• Data Analytics\n"
            "• Edge Computing\n"
            "• Cloud Integration\n"
            "• Industry Applications of AI & IoT\n\n"
            "Get details about the program, eligibility, curriculum, "
            "industry exposure, practical learning, and career opportunities.\n\n"
            "Please choose an option below 👇"
        )
    )

    footer = MessageFooter(
        text="🎓 GM University Admissions 2026-27"
    )

    action = ButtonAction(
        buttons=[
            Button(reply=ButtonReply(id="bgaaa", title="Program Details")),
            Button(reply=ButtonReply(id="bgaab", title="Fee Details")),
            Button(reply=ButtonReply(id="bgaac", title="More Info")),
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


def build_pgd_ai_iot_program_details_payload(wa_id: str):
    """Builds a WhatsApp text payload for PGD in AI & IoT with Intel program details."""

    text = (
        "🎓 *PGD in AI & IoT with Intel*\n"
        "📘 *Program Details – 2026-27 Intake*\n\n"
        "━━━━━━━━━━━━━━━\n"
        "📄 *Program Details Include:*\n"
        "• Curriculum Structure\n"
        "• Eligibility Criteria\n"
        "• Artificial Intelligence Concepts\n"
        "• Internet of Things Applications\n"
        "• Industry-Oriented Learning\n"
        "• Practical & Project-Based Training\n"
        "• Career Opportunities\n"
        "━━━━━━━━━━━━━━━\n\n"
        "📞 *Contact Details*\n"
        "━━━━━━━━━━━━━━━\n"
        "📍 GM University, Davangere\n"
        "☎️ Phone: +91 9364099712,+91 9364099720\n"
        # "📧 Email: info@gmu.ac.in"
    )

    payload = WhatsAppTextReplyRequest(
        to=wa_id,
        text=TextBody(
            body=text,
            preview_url=False
        ),
    )

    return payload.model_dump()


def build_pgd_ai_iot_fee_duration_payload(wa_id: str):
    """Builds a WhatsApp text payload for PGD in AI & IoT with Intel fee information."""

    text = (
        "🎓 *GM University – PGD in AI & IoT with Intel Fee Details*\n\n"
        
        "💰 *Program Fee:* ₹55,000\n\n"
        "📘 *Program Information:*\n"
        "━━━━━━━━━━━━━━━\n"
        "• Industry-focused postgraduate diploma program\n"
        "• Strong foundation in Artificial Intelligence and IoT technologies\n"
        "• Hands-on learning with modern tools and platforms\n"
        "• Practical training through projects and case studies\n"
        "• Career opportunities in AI, IoT, Data Analytics, Automation, and Smart Systems\n"
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


def build_pgd_ai_iot_more_info_payload(wa_id: str):
    """Builds a WhatsApp text payload for PGD in AI & IoT with Intel information."""

    text = (
        "🤖🌐 *GM University – PGD in AI & IoT with Intel*\n\n"
        "Learn advanced concepts and practical applications in:\n\n"
        "━━━━━━━━━━━━━━━\n"
        "• Artificial Intelligence\n"
        "• Machine Learning\n"
        "• Internet of Things\n"
        "• Embedded Systems\n"
        "• Data Analytics\n"
        "• Edge Computing\n"
        "• Cloud Technologies\n"
        "• Smart Automation Solutions\n"
        "━━━━━━━━━━━━━━━\n\n"
        "Enhance your skills with industry-relevant learning and hands-on projects."
    )

    payload = WhatsAppTextReplyRequest(
        to=wa_id,
        text=TextBody(
            body=text,
            preview_url=False
        ),
    )

    return payload.model_dump()

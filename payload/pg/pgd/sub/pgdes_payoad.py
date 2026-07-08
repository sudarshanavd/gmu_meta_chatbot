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

def build_pgd_embedded_systems_program_payload(wa_id: str):
    """Builds the payload for the PGD in Embedded Systems with Texas Instruments program."""

    header = MessageHeader(
        text="🔌⚙️ PGD in Embedded Systems with Texas Instruments"
    )

    body = MessageBody(
        text=(
            "🎓 *PGD in Embedded Systems with Texas Instruments*\n\n"
            "Learn core concepts in:\n"
            "• Embedded System Fundamentals\n"
            "• Microcontrollers and Microprocessors\n"
            "• Embedded C Programming\n"
            "• Digital Electronics\n"
            "• Real-Time Operating Systems (RTOS)\n"
            "• Hardware-Software Co-Design\n"
            "• Sensor and Interface Technologies\n"
            "• Embedded System Design and Development\n"
            "• IoT and Connected Devices\n"
            "• Industry Applications of Embedded Systems\n\n"
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
            Button(reply=ButtonReply(id="bgaba", title="Program Details")),
            Button(reply=ButtonReply(id="bgabb", title="Fee Details")),
            Button(reply=ButtonReply(id="bgabc", title="More Info")),
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


def build_pgd_embedded_systems_program_details_payload(wa_id: str):
    """Builds a WhatsApp text payload for PGD in Embedded Systems with Texas Instruments program details."""

    text = (
        "🎓 *PGD in Embedded Systems with Texas Instruments*\n"
        "📘 *Program Details – 2026-27 Intake*\n\n"
        "━━━━━━━━━━━━━━━\n"
        "📄 *Program Details Include:*\n"
        "• Curriculum Structure\n"
        "• Eligibility Criteria\n"
        "• Embedded Systems Concepts\n"
        "• Microcontroller and Processor Technologies\n"
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


def build_pgd_embedded_systems_fee_duration_payload(wa_id: str):
    """Builds a WhatsApp text payload for PGD in Embedded Systems with Texas Instruments fee information."""

    text = (
        "🎓 *GM University – PGD in Embedded Systems with Texas Instruments Fee Details*\n\n"
    
        "💰 *Program Fee:* ₹55,000\n\n"
        "📘 *Program Information:*\n"
        "━━━━━━━━━━━━━━━\n"
        "• Industry-focused postgraduate diploma program\n"
        "• Strong foundation in Embedded Systems and Hardware Design\n"
        "• Hands-on learning using industry-standard development tools\n"
        "• Practical training through projects and laboratory work\n"
        "• Career opportunities in Embedded Development, IoT, Electronics Design, Automation, and Semiconductor Industries\n"
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


def build_pgd_embedded_systems_more_info_payload(wa_id: str):
    """Builds a WhatsApp text payload for PGD in Embedded Systems with Texas Instruments information."""

    text = (
        "🔌⚙️ *GM University – PGD in Embedded Systems with Texas Instruments*\n\n"
        "Learn advanced concepts and practical applications in:\n\n"
        "━━━━━━━━━━━━━━━\n"
        "• Embedded Systems\n"
        "• Embedded C Programming\n"
        "• Microcontrollers\n"
        "• Real-Time Operating Systems\n"
        "• Digital Electronics\n"
        "• Hardware Interfacing\n"
        "• IoT Devices\n"
        "• Smart Embedded Solutions\n"
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
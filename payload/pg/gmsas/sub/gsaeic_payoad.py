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

def build_mtech_aeics_program_payload(wa_id: str):
    """Builds the payload for the M.Tech Advanced Electronics and Intelligent Communication Systems program."""

    header = MessageHeader(
        text="📡🤖 M.Tech Advanced Electronics and Intelligent Communication Systems"
    )

    body = MessageBody(
        text=(
            "🎓 *M.Tech in Advanced Electronics and Intelligent Communication Systems*\n\n"
            "Learn core concepts in:\n"
            "• Advanced Electronics Systems\n"
            "• Intelligent Communication Systems\n"
            "• Digital Signal Processing\n"
            "• VLSI Design\n"
            "• Embedded Systems\n"
            "• Wireless Communication\n"
            "• Internet of Things (IoT)\n"
            "• Antenna and RF Systems\n"
            "• AI in Communication Networks\n"
            "• Communication System Design\n\n"
            "Get details about the program, eligibility, curriculum, "
            "training, practical learning, and career opportunities.\n\n"
            "Please choose an option below 👇"
        )
    )

    footer = MessageFooter(
        text="🎓 GM University Admissions 2026-27"
    )

    btn_program_details = Button(reply=ButtonReply(id="baafa", title="Program Details"))
    btn_fee_duration = Button(reply=ButtonReply(id="baafb", title="Fee Details"))
    btn_branch_website = Button(reply=ButtonReply(id="baafc", title="More Info"))

    action = ButtonAction(buttons=[btn_program_details, btn_fee_duration, btn_branch_website])

    interactive = InteractiveButton(
        header=header,
        body=body,
        footer=footer,
        action=action,
    )

    payload = WhatsAppInteractiveButtonRequest(to=wa_id, interactive=interactive)
    return payload.model_dump()


def build_mtech_aeics_program_details_payload(wa_id: str):
    """Builds a well-formatted WhatsApp text payload for full M.Tech Advanced Electronics and Intelligent Communication Systems program details."""

    text = (
        "🎓 *M.Tech in Advanced Electronics and Intelligent Communication Systems*\n"
        "📘 *Program Details – 2026-27 Intake*\n\n"

        "━━━━━━━━━━━━━━━\n"
        "📄 *Program Document Includes:*\n"
        "• Curriculum Structure\n"
        "• Eligibility Criteria\n"
        "• Advanced Electronics Core Subjects\n"
        "• Intelligent Communication System Concepts\n"
        "• Practical & Industry-Oriented Learning\n"
        "• Academic & Career Opportunities\n"
        "━━━━━━━━━━━━━━━\n\n"

        "🔗 *View Full Program Document:*\n"
        "https://gmu.ac.in/imgview?dummy=data2024&base=assets%2Fdownloadmaterial%2FGMU%20School%20of%20Advanced%20%20Studies%20%20Pdf%20Final%2FM.Tech.inAdvancedElectronicsandIntelligentCommunicationSystems-ProgramDocument%2FM.Tech.inAdvancedElectronicsandIntelligentCommunicationSystems-ProgramDocument-&ext=png"
        "\n\n📞 *Contact Details*\n"
        "━━━━━━━━━━━━━━━\n"
        "📍 GM University, Davangere\n"
        "☎️ Phone: +91 9364099712,+91 9364099720\n"
        # "📧 Email: mtech.aeics@gmu.ac.in\n"
    )

    payload = WhatsAppTextReplyRequest(
        to=wa_id,
        text=TextBody(
            body=text,
            preview_url=True
        ),
    )

    return payload.model_dump()


def build_mtech_aeics_fee_duration_payload(wa_id: str):
    """Builds a well-formatted WhatsApp text payload for M.Tech Advanced Electronics and Intelligent Communication Systems fee information."""

    text = (
        "🎓 *GM University – M.Tech Advanced Electronics and Intelligent Communication Systems Fee Details*\n\n"

        "📌 Fee details\n"
        "━━━━━━━━━━━━━━━\n"
        "₹92,500\n\n"

        "⏳ *Program Duration*\n"
        "━━━━━━━━━━━━━━━\n"
        "3 Years \n\n"

        "📘 *Program Information:*\n"
        "━━━━━━━━━━━━━━━\n"
        "• Advanced electronics and communication focused program\n"
        "• Intelligent communication systems learning\n"
        "• Embedded, VLSI and wireless technology concepts\n"
        "• Industry-oriented electronics and communication practical training\n"
        "• Career opportunities in electronics, communication and intelligent systems sectors\n"
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


def build_mtech_aeics_branch_website_payload(wa_id: str):
    """Builds a well-formatted WhatsApp text payload for M.Tech Advanced Electronics and Intelligent Communication Systems information."""

    text = (
        "📡🤖 *GM University – M.Tech Advanced Electronics and Intelligent Communication Systems*\n\n"

        "📌 Official website/link will be updated soon.\n\n"

        "Stay connected with GM University for updates regarding:\n"
        "━━━━━━━━━━━━━━━\n"
        "• Program Overview\n"
        "• Curriculum Details\n"
        "• Practical Training\n"
        "• Electronics and Communication Lab Learning\n"
        "• Intelligent Communication Projects\n"
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
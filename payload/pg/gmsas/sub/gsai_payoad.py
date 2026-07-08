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

def build_mtech_aih_program_payload(wa_id: str):
    """Builds the payload for the M.Tech AI in Healthcare program."""

    header = MessageHeader(
        text="🤖🏥 M.Tech AI in Healthcare"
    )

    body = MessageBody(
        text=(
            "🎓 *M.Tech in AI in Healthcare*\n\n"
            "Learn core concepts in:\n"
            "• Artificial Intelligence in Healthcare\n"
            "• Machine Learning for Medical Data\n"
            "• Deep Learning in Medical Imaging\n"
            "• Healthcare Data Analytics\n"
            "• Clinical Decision Support Systems\n"
            "• Medical Image Processing\n"
            "• Natural Language Processing in Healthcare\n"
            "• Digital Health Technologies\n"
            "• Biomedical Data Management\n"
            "• AI Ethics and Healthcare Regulations\n\n"
            "Get details about the program, eligibility, curriculum, "
            "training, practical learning, and career opportunities.\n\n"
            "Please choose an option below 👇"
        )
    )

    footer = MessageFooter(
        text="🎓 GM University Admissions 2026-27"
    )

    btn_program_details = Button(reply=ButtonReply(id="baaba", title="Program Details"))
    btn_fee_duration = Button(reply=ButtonReply(id="baabb", title="Fee Details"))
    btn_branch_website = Button(reply=ButtonReply(id="baabc", title="More Info"))

    action = ButtonAction(buttons=[btn_program_details, btn_fee_duration, btn_branch_website])

    interactive = InteractiveButton(
        header=header,
        body=body,
        footer=footer,
        action=action,
    )

    payload = WhatsAppInteractiveButtonRequest(to=wa_id, interactive=interactive)
    return payload.model_dump()


def build_mtech_aih_program_details_payload(wa_id: str):
    """Builds a well-formatted WhatsApp text payload for full M.Tech AI in Healthcare program details."""

    text = (
        "🎓 *M.Tech in AI in Healthcare*\n"
        "📘 *Program Details – 2026-27 Intake*\n\n"

        "━━━━━━━━━━━━━━━\n"
        "📄 *Program Document Includes:*\n"
        "• Curriculum Structure\n"
        "• Eligibility Criteria\n"
        "• AI in Healthcare Core Subjects\n"
        "• Healthcare Data & Medical AI Concepts\n"
        "• Practical & Industry-Oriented Learning\n"
        "• Academic & Career Opportunities\n"
        "━━━━━━━━━━━━━━━\n\n"

        "🔗 *View Full Program Document:*\n"
        "https://gmu.ac.in/imgview?dummy=data2024&base=assets%2Fdownloadmaterial%2FGMU%20School%20of%20Advanced%20%20Studies%20%20Pdf%20Final%2FProgram%20Details%20AIHC%2FProgram%20Details%20AIHC-&ext=png"

        "\n\n📞 *Contact Details*\n"
        "━━━━━━━━━━━━━━━\n"
        "📍 GM University, Davangere\n"
        "☎️ Phone: +91 9364099712,+91 9364099720\n"
        # "📧 Email: mtech.aihealthcare@gmu.ac.in\n"
    )

    payload = WhatsAppTextReplyRequest(
        to=wa_id,
        text=TextBody(
            body=text,
            preview_url=True
        ),
    )

    return payload.model_dump()


def build_mtech_aih_fee_duration_payload(wa_id: str):
    """Builds a well-formatted WhatsApp text payload for M.Tech AI in Healthcare fee information."""

    text = (
        "🎓 *GM University – M.Tech AI in Healthcare Fee Details*\n\n"

        "📌 Fee details\n"
        "━━━━━━━━━━━━━━━\n"
        "₹1,25,000\n\n"

        "⏳ *Program Duration*\n"
        "━━━━━━━━━━━━━━━\n"
        "2 Years \n\n"

        "📘 *Program Information:*\n"
        "━━━━━━━━━━━━━━━\n"
        "• Advanced AI and healthcare focused program\n"
        "• Medical data analytics and AI model training\n"
        "• Clinical decision support and medical imaging applications\n"
        "• Python-based practical learning\n"
        "• Career opportunities in AI, healthcare technology and research sectors\n"
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


def build_mtech_aih_branch_website_payload(wa_id: str):
    """Builds a well-formatted WhatsApp text payload for M.Tech AI in Healthcare information."""

    text = (
        "🤖🏥 *GM University – M.Tech AI in Healthcare*\n\n"

        "📌 Official website/link will be updated soon.\n\n"

        "Stay connected with GM University for updates regarding:\n"
        "━━━━━━━━━━━━━━━\n"
        "• Program Overview\n"
        "• Curriculum Details\n"
        "• Practical Training\n"
        "• AI Healthcare Lab Learning\n"
        "• Medical AI Projects\n"
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
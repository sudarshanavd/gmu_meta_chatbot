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


def build_mtech_pdm_program_payload(wa_id: str):
    """Builds the payload for the M.Tech Product Development and Marketing program."""

    header = MessageHeader(
        text="🛠️📈 M.Tech Product Development and Marketing"
    )

    body = MessageBody(
        text=(
            "🎓 *M.Tech in Product Development and Marketing*\n\n"
            "Learn core concepts in:\n"
            "• Product Design\n"
            "• Product Development Process\n"
            "• Innovation Management\n"
            "• Design Thinking\n"
            "• Market Research\n"
            "• Consumer Behaviour\n"
            "• Branding and Promotion\n"
            "• Digital Marketing\n"
            "• Product Lifecycle Management\n"
            "• Entrepreneurship and Business Strategy\n\n"
            "Get details about the program, eligibility, curriculum, "
            "training, practical learning, and career opportunities.\n\n"
            "Please choose an option below 👇"
        )
    )

    footer = MessageFooter(
        text="🎓 GM University Admissions 2026-27"
    )

    btn_program_details = Button(reply=ButtonReply(id="baaha", title="Program Details"))
    btn_fee_duration = Button(reply=ButtonReply(id="baahb", title="Fee Details"))
    btn_branch_website = Button(reply=ButtonReply(id="baahc", title="More Info"))

    action = ButtonAction(buttons=[btn_program_details, btn_fee_duration, btn_branch_website])

    interactive = InteractiveButton(
        header=header,
        body=body,
        footer=footer,
        action=action,
    )

    payload = WhatsAppInteractiveButtonRequest(to=wa_id, interactive=interactive)
    return payload.model_dump()


def build_mtech_pdm_program_details_payload(wa_id: str):
    """Builds a WhatsApp text payload for M.Tech Product Development and Marketing program details."""

    text = (
        "🎓 *M.Tech in Product Development and Marketing*\n"
        "📘 *Program Details – 2026-27 Intake*\n\n"

        "━━━━━━━━━━━━━━━\n"
        "📄 *Program Document Includes:*\n"
        "• Curriculum Structure\n"
        "• Eligibility Criteria\n"
        "• Product Development Core Subjects\n"
        "• Marketing and Branding Concepts\n"
        "• Practical & Industry-Oriented Learning\n"
        "• Innovation, Entrepreneurship and Career Opportunities\n"
        "━━━━━━━━━━━━━━━\n\n"

        "🔗 *View Full Program Document:*\n"
        "https://gmu.ac.in/pdfview_assets%5Cdownloadmaterial%5CGMU%20School%20of%20Advanced%20%20Studies%20%20Pdf%20Final%5CProgram%20Documents%20-PDM.pdf"
        "\n\n📞 *Contact Details*\n"
        "━━━━━━━━━━━━━━━\n"
        "📍 GM University, Davangere\n"
        "☎️ Phone: +91 9364099712,+91 9364099720\n"
        # "📧 Email: info@gmu.ac.in\n"
    )

    payload = WhatsAppTextReplyRequest(
        to=wa_id,
        text=TextBody(
            body=text,
            preview_url=True
        ),
    )

    return payload.model_dump()


def build_mtech_pdm_fee_duration_payload(wa_id: str):
    """Builds a WhatsApp text payload for M.Tech Product Development and Marketing fee information."""

    text = (
        "🎓 *GM University – M.Tech Product Development and Marketing Fee Details*\n\n"

        "📌 Fee details\n"
        "━━━━━━━━━━━━━━━\n"
        "₹1,25,000\n\n"

        "⏳ *Program Duration*\n"
        "━━━━━━━━━━━━━━━\n"
        "2 Years \n\n"

        "📘 *Program Information:*\n"
        "━━━━━━━━━━━━━━━\n"
        "• Product development and innovation focused program\n"
        "• Marketing, branding and customer-focused learning\n"
        "• Design thinking and product lifecycle concepts\n"
        "• Industry-oriented practical training\n"
        "• Career opportunities in product management, marketing, innovation and business strategy\n"
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


def build_mtech_pdm_branch_website_payload(wa_id: str):
    """Builds a WhatsApp text payload for M.Tech Product Development and Marketing information."""

    text = (
        "🛠️📈 *GM University – M.Tech Product Development and Marketing*\n\n"

        "🔗 *Official Program Document:*\n"
        "https://gmu.ac.in/pdfview_assets%5Cdownloadmaterial%5CGMU%20School%20of%20Advanced%20%20Studies%20%20Pdf%20Final%5CProgram%20Documents%20-PDM.pdf\n\n"

        "Stay connected with GM University for updates regarding:\n"
        "━━━━━━━━━━━━━━━\n"
        "• Program Overview\n"
        "• Curriculum Details\n"
        "• Practical Training\n"
        "• Product Development Projects\n"
        "• Marketing and Branding Learning\n"
        "• Admission Information\n"
        "• Student Resources\n"
        "━━━━━━━━━━━━━━━"
    )

    payload = WhatsAppTextReplyRequest(
        to=wa_id,
        text=TextBody(
            body=text,
            preview_url=True
        ),
    )

    return payload.model_dump()
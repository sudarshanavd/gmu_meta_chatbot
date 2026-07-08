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


def build_mtech_sga_program_payload(wa_id: str):
    """Builds the payload for the M.Tech Smart and Green Agriculture program."""

    header = MessageHeader(
        text="🌱🤖 M.Tech Smart and Green Agriculture"
    )

    body = MessageBody(
        text=(
            "🎓 *M.Tech in Smart and Green Agriculture*\n\n"
            "Learn core concepts in:\n"
            "• Smart Farming Technologies\n"
            "• Green and Sustainable Agriculture\n"
            "• Precision Agriculture\n"
            "• IoT in Agriculture\n"
            "• AI and Data Analytics for Farming\n"
            "• Soil and Water Management\n"
            "• Renewable Energy in Agriculture\n"
            "• Agri Automation\n"
            "• Climate-Smart Agriculture\n"
            "• Sustainable Food Production\n\n"
            "Get details about the program, eligibility, curriculum, "
            "training, practical learning, and career opportunities.\n\n"
            "Please choose an option below 👇"
        )
    )

    footer = MessageFooter(
        text="🎓 GM University Admissions 2026-27"
    )

    btn_program_details = Button(reply=ButtonReply(id="baaia", title="Program Details"))
    btn_fee_duration = Button(reply=ButtonReply(id="baaib", title="Fee Details"))
    btn_branch_website = Button(reply=ButtonReply(id="baaic", title="More Info"))

    action = ButtonAction(buttons=[btn_program_details, btn_fee_duration, btn_branch_website])

    interactive = InteractiveButton(
        header=header,
        body=body,
        footer=footer,
        action=action,
    )

    payload = WhatsAppInteractiveButtonRequest(to=wa_id, interactive=interactive)
    return payload.model_dump()


def build_mtech_sga_program_details_payload(wa_id: str):
    """Builds a WhatsApp text payload for M.Tech Smart and Green Agriculture program details."""

    text = (
        "🎓 *M.Tech in Smart and Green Agriculture*\n"
        "📘 *Program Details – 2026-27 Intake*\n\n"

        "━━━━━━━━━━━━━━━\n"
        "📄 *Program Document Includes:*\n"
        "• Curriculum Structure\n"
        "• Eligibility Criteria\n"
        "• Smart Agriculture Core Subjects\n"
        "• Green and Sustainable Farming Concepts\n"
        "• AI, IoT and Automation in Agriculture\n"
        "• Practical & Industry-Oriented Learning\n"
        "• Research and Career Opportunities\n"
        "━━━━━━━━━━━━━━━\n\n"

        "🔗 *View Full Program Document:*\n"
        "https://gmu.ac.in/pdfview_assets%5Cdownloadmaterial%5CGMU%20School%20of%20Advanced%20%20Studies%20%20Pdf%20Final%5CProgram%20Document%20-SGA.pdf"

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


def build_mtech_sga_fee_duration_payload(wa_id: str):
    """Builds a WhatsApp text payload for M.Tech Smart and Green Agriculture fee information."""

    text = (
        "🎓 *GM University – M.Tech Smart and Green Agriculture Fee Details*\n\n"

        "⏱ *Duration:* 2 Years\n"
        "💰 *Program Annual Fee:* ₹1,25,000\n\n"

        "📘 *Program Information:*\n"
        "━━━━━━━━━━━━━━━\n"
        "• Smart farming and sustainable agriculture focused program\n"
        "• AI, IoT and data-driven agriculture learning\n"
        "• Green technology and eco-friendly farming concepts\n"
        "• Industry-oriented practical training\n"
        "• Career opportunities in agri-tech, smart farming, sustainability and research\n"
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


def build_mtech_sga_branch_website_payload(wa_id: str):
    """Builds a WhatsApp text payload for M.Tech Smart and Green Agriculture information."""

    text = (
        "🌱🤖 *GM University – M.Tech Smart and Green Agriculture*\n\n"

        "🔗 *Official Program Document:*\n"
        "https://gmu.ac.in/pdfview_assets%5Cdownloadmaterial%5CGMU%20School%20of%20Advanced%20%20Studies%20%20Pdf%20Final%5CProgram%20Document%20-SGA.pdf"
        "Stay connected with GM University for updates regarding:\n"
        "━━━━━━━━━━━━━━━\n"
        "• Program Overview\n"
        "• Curriculum Details\n"
        "• Practical Training\n"
        "• Smart Agriculture Projects\n"
        "• Green Farming Technologies\n"
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
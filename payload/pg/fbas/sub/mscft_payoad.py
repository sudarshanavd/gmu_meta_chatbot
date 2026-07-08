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

def build_msc_food_technology_program_payload(wa_id: str):
    """Builds the payload for the M.Sc Food Technology program."""

    header = MessageHeader(
        text="🍽️🔬 M.Sc Food Technology"
    )

    body = MessageBody(
        text=(
            "🎓 *M.Sc in Food Technology*\n\n"
            "Learn core concepts in:\n"
            "• Food Chemistry\n"
            "• Food Microbiology\n"
            "• Food Processing Technology\n"
            "• Food Preservation\n"
            "• Food Quality Control\n"
            "• Food Safety and Hygiene\n"
            "• Nutrition and Dietetics\n"
            "• Dairy and Bakery Technology\n"
            "• Food Packaging Technology\n"
            "• Research Methodology\n\n"
            "Get details about the program, eligibility, curriculum, "
            "laboratory learning, industry training, and career opportunities.\n\n"
            "Please choose an option below 👇"
        )
    )

    footer = MessageFooter(
        text="🎓 GM University Admissions 2026-27"
    )

    btn_program_details = Button(reply=ButtonReply(id="fbada", title="Program Details"))
    btn_fee_duration = Button(reply=ButtonReply(id="fbadb", title="Fee Details"))
    btn_branch_website = Button(reply=ButtonReply(id="fbadc", title="More Info"))

    action = ButtonAction(buttons=[btn_program_details, btn_fee_duration, btn_branch_website])

    interactive = InteractiveButton(
        header=header,
        body=body,
        footer=footer,
        action=action,
    )

    payload = WhatsAppInteractiveButtonRequest(to=wa_id, interactive=interactive)
    return payload.model_dump()


def build_msc_food_technology_program_details_payload(wa_id: str):
    """Builds a WhatsApp text payload for M.Sc Food Technology program details."""

    text = (
        "🎓 *M.Sc in Food Technology*\n"
        "📘 *Program Details – 2026-27 Intake*\n\n"

        "━━━━━━━━━━━━━━━\n"
        "📄 *Program Document Includes:*\n"
        "• Curriculum Structure\n"
        "• Eligibility Criteria\n"
        "• Food Technology Core Subjects\n"
        "• Food Processing and Preservation Concepts\n"
        "• Laboratory and Industrial Learning\n"
        "• Practical & Academic Training\n"
        "• Higher Studies and Career Opportunities\n"
        "━━━━━━━━━━━━━━━\n\n"

        "🔗 *View Full Program Document:*\n"
        "https://gmu.ac.in/pdfview_assets%5Cdownloadmaterial%5CSchool%20of%20Applied%20Sciences-%20Program%20Docs%5CGMU-%20Course%20Details%20M.Sc%20Food%20Technology.pdf"

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


def build_msc_food_technology_fee_duration_payload(wa_id: str):
    """Builds a WhatsApp text payload for M.Sc Food Technology fee information."""

    text = (
        "🎓 *GM University – M.Sc Food Technology Fee Details*\n\n"

        "⏱ *Duration:* 2 Years\n"
        "💰 *Program Annual Fee:* ₹75,000\n\n"

        "📘 *Program Information:*\n"
        "━━━━━━━━━━━━━━━\n"
        "• Advanced food science and technology focused postgraduate program\n"
        "• Strong foundation in food processing, preservation and safety\n"
        "• Laboratory-based practical learning\n"
        "• Industry and research-oriented training\n"
        "• Career opportunities in food industries, quality control, food safety, research and higher studies\n"
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


def build_msc_food_technology_branch_website_payload(wa_id: str):
    """Builds a WhatsApp text payload for M.Sc Food Technology information."""

    text = (
        "🍽️🔬 *GM University – M.Sc Food Technology*\n\n"

        "🔗 *Official Program Document:*\n"
        "https://gmu.ac.in/pdfview_assets%5Cdownloadmaterial%5CSchool%20of%20Applied%20Sciences-%20Program%20Docs%5CGMU-%20Course%20Details%20M.Sc%20Food%20Technology.pdf\n\n"

        "Stay connected with GM University for updates regarding:\n"
        "━━━━━━━━━━━━━━━\n"
        "• Program Overview\n"
        "• Curriculum Details\n"
        "• Laboratory Learning\n"
        "• Food Processing Projects\n"
        "• Industry Training\n"
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
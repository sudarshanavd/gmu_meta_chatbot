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

def build_msc_mathematics_program_payload(wa_id: str):
    """Builds the payload for the M.Sc Mathematics program."""

    header = MessageHeader(
        text="📐➗ M.Sc Mathematics"
    )

    body = MessageBody(
        text=(
            "🎓 *M.Sc in Mathematics*\n\n"
            "Learn core concepts in:\n"
            "• Real Analysis\n"
            "• Complex Analysis\n"
            "• Abstract Algebra\n"
            "• Differential Equations\n"
            "• Linear Algebra\n"
            "• Topology\n"
            "• Numerical Methods\n"
            "• Mathematical Modelling\n"
            "• Probability and Statistics\n"
            "• Research Methodology\n\n"
            "Get details about the program, eligibility, curriculum, "
            "analytical learning, research training, and career opportunities.\n\n"
            "Please choose an option below 👇"
        )
    )

    footer = MessageFooter(
        text="🎓 GM University Admissions 2026-27"
    )

    btn_program_details = Button(reply=ButtonReply(id="fbaca", title="Program Details"))
    btn_fee_duration = Button(reply=ButtonReply(id="fbacb", title="Fee Details"))
    btn_branch_website = Button(reply=ButtonReply(id="fbacc", title="More Info"))

    action = ButtonAction(buttons=[btn_program_details, btn_fee_duration, btn_branch_website])

    interactive = InteractiveButton(
        header=header,
        body=body,
        footer=footer,
        action=action,
    )

    payload = WhatsAppInteractiveButtonRequest(to=wa_id, interactive=interactive)
    return payload.model_dump()


def build_msc_mathematics_program_details_payload(wa_id: str):
    """Builds a WhatsApp text payload for M.Sc Mathematics program details."""

    text = (
        "🎓 *M.Sc in Mathematics*\n"
        "📘 *Program Details – 2026-27 Intake*\n\n"

        "━━━━━━━━━━━━━━━\n"
        "📄 *Program Document Includes:*\n"
        "• Curriculum Structure\n"
        "• Eligibility Criteria\n"
        "• Mathematics Core Subjects\n"
        "• Analytical and Computational Learning\n"
        "• Research Methodology\n"
        "• Practical & Academic Training\n"
        "• Higher Studies and Career Opportunities\n"
        "━━━━━━━━━━━━━━━\n\n"

        "🔗 *View Full Program Document:*\n"
        "https://gmu.ac.in/pdfview_assets%5Cdownloadmaterial%5CSchool%20of%20Mathematical%20and%20Physical%20Sciences-Program%20Docs%5CMSc%20-%20Mathematics%20-%20Course%20Document.pdf"
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


def build_msc_mathematics_fee_duration_payload(wa_id: str):
    """Builds a WhatsApp text payload for M.Sc Mathematics fee information."""

    text = (
        "🎓 *GM University – M.Sc Mathematics Fee Details*\n\n"

        "⏱ *Duration:* 2 Years\n"
        "💰 *Program Annual Fee:* ₹75,000\n\n"

        "📘 *Program Information:*\n"
        "━━━━━━━━━━━━━━━\n"
        "• Advanced mathematics and research-focused postgraduate program\n"
        "• Strong foundation in algebra, analysis and applied mathematics\n"
        "• Analytical and computational learning\n"
        "• Academic and research-oriented training\n"
        "• Career opportunities in teaching, research, data analytics, finance, IT and higher studies\n"
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


def build_msc_mathematics_branch_website_payload(wa_id: str):
    """Builds a WhatsApp text payload for M.Sc Mathematics information."""

    text = (
        "📐➗ *GM University – M.Sc Mathematics*\n\n"

        "🔗 *Official Program Document:*\n"
        "https://gmu.ac.in/pdfview_assets%5Cdownloadmaterial%5CSchool%20of%20Mathematical%20and%20Physical%20Sciences-Program%20Docs%5CMSc%20-%20Mathematics%20-%20Course%20Document.pdf\n\n"

        "Stay connected with GM University for updates regarding:\n"
        "━━━━━━━━━━━━━━━\n"
        "• Program Overview\n"
        "• Curriculum Details\n"
        "• Analytical Learning\n"
        "• Mathematics Research Projects\n"
        "• Academic Training\n"
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
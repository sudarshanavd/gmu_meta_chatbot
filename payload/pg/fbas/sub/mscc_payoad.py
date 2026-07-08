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

def build_msc_chemistry_program_payload(wa_id: str):
    """Builds the payload for the M.Sc Chemistry program."""

    header = MessageHeader(
        text="🧪⚗️ M.Sc Chemistry"
    )

    body = MessageBody(
        text=(
            "🎓 *M.Sc in Chemistry*\n\n"
            "Learn core concepts in:\n"
            "• Organic Chemistry\n"
            "• Inorganic Chemistry\n"
            "• Physical Chemistry\n"
            "• Analytical Chemistry\n"
            "• Industrial Chemistry\n"
            "• Spectroscopy\n"
            "• Polymer Chemistry\n"
            "• Environmental Chemistry\n"
            "• Biochemistry\n"
            "• Research Methodology\n\n"
            "Get details about the program, eligibility, curriculum, "
            "laboratory learning, research training, and career opportunities.\n\n"
            "Please choose an option below 👇"
        )
    )

    footer = MessageFooter(
        text="🎓 GM University Admissions 2026-27"
    )

    btn_program_details = Button(reply=ButtonReply(id="fbaba", title="Program Details"))
    btn_fee_duration = Button(reply=ButtonReply(id="fbabb", title="Fee Details"))
    btn_branch_website = Button(reply=ButtonReply(id="fbabc", title="More Info"))

    action = ButtonAction(buttons=[btn_program_details, btn_fee_duration, btn_branch_website])

    interactive = InteractiveButton(
        header=header,
        body=body,
        footer=footer,
        action=action,
    )

    payload = WhatsAppInteractiveButtonRequest(to=wa_id, interactive=interactive)
    return payload.model_dump()


def build_msc_chemistry_program_details_payload(wa_id: str):
    """Builds a WhatsApp text payload for M.Sc Chemistry program details."""

    text = (
        "🎓 *M.Sc in Chemistry*\n"
        "📘 *Program Details – 2026-27 Intake*\n\n"

        "━━━━━━━━━━━━━━━\n"
        "📄 *Program Document Includes:*\n"
        "• Curriculum Structure\n"
        "• Eligibility Criteria\n"
        "• Chemistry Core Subjects\n"
        "• Laboratory and Experimental Learning\n"
        "• Research Methodology\n"
        "• Practical & Academic Training\n"
        "• Higher Studies and Career Opportunities\n"
        "━━━━━━━━━━━━━━━\n\n"

        "🔗 *View Full Program Document:*\n"
        "https://gmu.ac.in/pdfview_assets%5Cdownloadmaterial%5CSchool%20of%20Chemical%20and%20Biological%20Sciences-Program%20Docs%5CFinal%20M.Sc.%20Course_%20Contents%202024-25.pdf"

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


def build_msc_chemistry_fee_duration_payload(wa_id: str):
    """Builds a WhatsApp text payload for M.Sc Chemistry fee information."""

    text = (
        "🎓 *GM University – M.Sc Chemistry Fee Details*\n\n"

        "⏱ *Duration:* 2 Years\n"
        "💰 *Program Annual Fee:* ₹75,000\n\n"

        "📘 *Program Information:*\n"
        "━━━━━━━━━━━━━━━\n"
        "• Advanced chemistry and research-focused postgraduate program\n"
        "• Strong foundation in organic, inorganic and physical chemistry\n"
        "• Laboratory-based practical learning\n"
        "• Academic and research-oriented training\n"
        "• Career opportunities in research, pharmaceuticals, chemical industries, laboratories and higher studies\n"
        "━━━━━━━━━━━━━━━"
        "\n📞 *Contact Details*\n"
        "━━━━━━━━━━━━━━━\n"
        "📍 GM University, Davangere\n"
        "☎️ Phone: +91 XXXXX XXXXX\n"
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


def build_msc_chemistry_branch_website_payload(wa_id: str):
    """Builds a WhatsApp text payload for M.Sc Chemistry information."""

    text = (
        "🧪⚗️ *GM University – M.Sc Chemistry*\n\n"

        "🔗 *Official Program Document:*\n"
        "https://gmu.ac.in/pdfview_assets%5Cdownloadmaterial%5CSchool%20of%20Chemical%20and%20Biological%20Sciences-Program%20Docs%5CFinal%20M.Sc.%20Course_%20Contents%202024-25.pdf\n\n"

        "Stay connected with GM University for updates regarding:\n"
        "━━━━━━━━━━━━━━━\n"
        "• Program Overview\n"
        "• Curriculum Details\n"
        "• Laboratory Learning\n"
        "• Chemistry Research Projects\n"
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
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


def build_msc_physics_program_payload(wa_id: str):
    """Builds the payload for the M.Sc Physics program."""

    header = MessageHeader(
        text="🔭⚛️ M.Sc Physics"
    )

    body = MessageBody(
        text=(
            "🎓 *M.Sc in Physics*\n\n"
            "Learn core concepts in:\n"
            "• Classical Mechanics\n"
            "• Quantum Mechanics\n"
            "• Electrodynamics\n"
            "• Statistical Mechanics\n"
            "• Mathematical Physics\n"
            "• Solid State Physics\n"
            "• Nuclear Physics\n"
            "• Electronics\n"
            "• Optics and Spectroscopy\n"
            "• Research Methodology\n\n"
            "Get details about the program, eligibility, curriculum, "
            "laboratory learning, research training, and career opportunities.\n\n"
            "Please choose an option below 👇"
        )
    )

    footer = MessageFooter(
        text="🎓 GM University Admissions 2026-27"
    )

    btn_program_details = Button(reply=ButtonReply(id="fbaaa", title="Program Details"))
    btn_fee_duration = Button(reply=ButtonReply(id="fbaab", title="Fee Details"))
    btn_branch_website = Button(reply=ButtonReply(id="fbaac", title="More Info"))

    action = ButtonAction(buttons=[btn_program_details, btn_fee_duration, btn_branch_website])

    interactive = InteractiveButton(
        header=header,
        body=body,
        footer=footer,
        action=action,
    )

    payload = WhatsAppInteractiveButtonRequest(to=wa_id, interactive=interactive)
    return payload.model_dump()


def build_msc_physics_program_details_payload(wa_id: str):
    """Builds a WhatsApp text payload for M.Sc Physics program details."""

    text = (
        "🎓 *M.Sc in Physics*\n"
        "📘 *Program Details – 2026-27 Intake*\n\n"

        "━━━━━━━━━━━━━━━\n"
        "📄 *Program Document Includes:*\n"
        "• Curriculum Structure\n"
        "• Eligibility Criteria\n"
        "• Physics Core Subjects\n"
        "• Laboratory and Experimental Learning\n"
        "• Research Methodology\n"
        "• Practical & Academic Training\n"
        "• Higher Studies and Career Opportunities\n"
        "━━━━━━━━━━━━━━━\n\n"

        "🔗 *View Full Program Document:*\n"
        "https://gmu.ac.in/pdfview_assets%5Cdownloadmaterial%5CSchool%20of%20Mathematical%20and%20Physical%20Sciences-Program%20Docs%5CMSc%20-%20Physics%20-%20Course%20Document.pdf"
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


def build_msc_physics_fee_duration_payload(wa_id: str):
    """Builds a WhatsApp text payload for M.Sc Physics fee information."""

    text = (
        "🎓 *GM University – M.Sc Physics Fee Details*\n\n"

        "⏱ *Duration:* 2 Years\n"
        "💰 *Program Annual Fee:* ₹75,000\n\n"

        "📘 *Program Information:*\n"
        "━━━━━━━━━━━━━━━\n"
        "• Advanced physics and research-focused postgraduate program\n"
        "• Strong foundation in classical, quantum and statistical physics\n"
        "• Laboratory-based practical learning\n"
        "• Academic and research-oriented training\n"
        "• Career opportunities in teaching, research, laboratories, industries and higher studies\n"
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

    return payload.model_dump()


def build_msc_physics_branch_website_payload(wa_id: str):
    """Builds a WhatsApp text payload for M.Sc Physics information."""

    text = (
        "🔭⚛️ *GM University – M.Sc Physics*\n\n"

        "🔗 *Official Program Document:*\n"
        "https://gmu.ac.in/pdfview_assets%5Cdownloadmaterial%5CSchool%20of%20Mathematical%20and%20Physical%20Sciences-Program%20Docs%5CMSc%20-%20Physics%20-%20Course%20Document.pdf\n\n"

        "Stay connected with GM University for updates regarding:\n"
        "━━━━━━━━━━━━━━━\n"
        "• Program Overview\n"
        "• Curriculum Details\n"
        "• Laboratory Learning\n"
        "• Physics Research Projects\n"
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
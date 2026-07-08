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

def build_bvoc_ecdm_program_payload(wa_id: str):
    """Builds the payload for the B.Voc E-Commerce and Digital Marketing program."""

    header = MessageHeader(
        text="🛒📱 B.Voc E-Commerce and Digital Marketing"
    )

    body = MessageBody(
        text=(
            "🎓 *B.Voc in E-Commerce and Digital Marketing*\n\n"
            "Learn core concepts in:\n"
            "• E-Commerce Fundamentals\n"
            "• Digital Marketing Strategies\n"
            "• Search Engine Optimization (SEO)\n"
            "• Social Media Marketing\n"
            "• Content Marketing\n"
            "• Online Advertising\n"
            "• E-Commerce Website Management\n"
            "• Customer Relationship Management\n"
            "• Web Analytics\n"
            "• Digital Sales and Branding\n\n"
            "Get details about the program, eligibility, curriculum, "
            "training, practical learning, and career opportunities.\n\n"
            "Please choose an option below 👇"
        )
    )

    footer = MessageFooter(
        text="🎓 GM University Admissions 2026-27"
    )

    btn_program_details = Button(reply=ButtonReply(id="agaea", title="Program Details"))
    btn_fee_duration = Button(reply=ButtonReply(id="agaeb", title="Fee Details"))
    btn_branch_website = Button(reply=ButtonReply(id="agaec", title="More Info"))

    action = ButtonAction(buttons=[btn_program_details, btn_fee_duration, btn_branch_website])

    interactive = InteractiveButton(
        header=header,
        body=body,
        footer=footer,
        action=action,
    )

    payload = WhatsAppInteractiveButtonRequest(to=wa_id, interactive=interactive)
    return payload.model_dump()


def build_bvoc_ecdm_program_details_payload(wa_id: str):
    """Builds a well-formatted WhatsApp text payload for full B.Voc E-Commerce and Digital Marketing program details."""

    text = (
        "🎓 *B.Voc in E-Commerce and Digital Marketing*\n"
        "📘 *Program Details – 2026-27 Intake*\n\n"

        "━━━━━━━━━━━━━━━\n"
        "📄 *Program Document Includes:*\n"
        "• Curriculum Structure\n"
        "• Eligibility Criteria\n"
        "• E-Commerce Core Subjects\n"
        "• Digital Marketing Training\n"
        "• Practical & Industry-Oriented Learning\n"
        "• Academic & Career Opportunities\n"
        "━━━━━━━━━━━━━━━\n\n"

        "🔗 *View Full Program Document:*\n"
        "https://gmu.ac.in/pdfview_assets%5Cdownloadmaterial%5CB%20Voc%20Programs%202026-27%5CB%20Voc%20-%20Program%20Document%20-%202026-27%5CPROGRAM%20DOCUMENT-ECDM-FINAL.pdf"

        "\n\n📞 *Contact Details*\n"
        "━━━━━━━━━━━━━━━\n"
        "📍 GM University, Davangere\n"
        "☎️ Phone: +91 9364099712,+91 9364099720\n"
        # "📧 Email: bvoc.ecdm@gmu.ac.in\n"
    )

    payload = WhatsAppTextReplyRequest(
        to=wa_id,
        text=TextBody(
            body=text,
            preview_url=True
        ),
    )

    return payload.model_dump()


def build_bvoc_ecdm_fee_duration_payload(wa_id: str):
    """Builds a well-formatted WhatsApp text payload for B.Voc E-Commerce and Digital Marketing fee information."""

    text = (
        "🎓 *GM University – B.Voc E-Commerce and Digital Marketing Fee Details*\n\n"

        "📌 Fee details will be updated by the university admission office.\n\n"

        "📘 *Program Information:*\n"
        "━━━━━━━━━━━━━━━\n"
        "• Skill-based vocational program\n"
        "• E-commerce platform training\n"
        "• Digital marketing practical learning\n"
        "• Online business and branding skills\n"
        "• Career opportunities in e-commerce and digital marketing sectors\n"
        "━━━━━━━━━━━━━━━\n\n"

        "📞 *Contact Details*\n"
        "━━━━━━━━━━━━━━━\n"
        "📍 GM University, Davangere\n"
        "☎️ Phone: +91 9364099712,+91 9364099720\n"
        # "📧 Email: bvoc.ecdm@gmu.ac.in\n"
    )

    payload = WhatsAppTextReplyRequest(
        to=wa_id,
        text=TextBody(
            body=text,
            preview_url=False
        ),
    )

    return payload.model_dump()


def build_bvoc_ecdm_branch_website_payload(wa_id: str):
    """Builds a well-formatted WhatsApp text payload for B.Voc E-Commerce and Digital Marketing information."""

    text = (
        "🛒📱 *GM University – B.Voc E-Commerce and Digital Marketing*\n\n"

        "📌 Official website/link will be updated soon.\n\n"

        "Stay connected with GM University for updates regarding:\n"
        "━━━━━━━━━━━━━━━\n"
        "• Program Overview\n"
        "• Curriculum Details\n"
        "• Practical Training\n"
        "• E-Commerce Platform Learning\n"
        "• Digital Marketing Workshops\n"
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
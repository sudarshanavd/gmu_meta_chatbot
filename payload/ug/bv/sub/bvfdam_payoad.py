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

def build_bvoc_fdam_program_payload(wa_id: str):
    """Builds the payload for the B.Voc Fashion Design and Apparel Manufacture program."""

    header = MessageHeader(
        text="👗🧵 B.Voc Fashion Design and Apparel Manufacture"
    )

    body = MessageBody(
        text=(
            "🎓 *B.Voc in Fashion Design and Apparel Manufacture*\n\n"
            "Learn core concepts in:\n"
            "• Fashion Design Fundamentals\n"
            "• Textile Science\n"
            "• Apparel Manufacturing\n"
            "• Pattern Making\n"
            "• Garment Construction\n"
            "• Fashion Illustration\n"
            "• Computer Aided Fashion Design\n"
            "• Fabric Selection & Testing\n"
            "• Quality Control in Apparel\n"
            "• Fashion Merchandising\n\n"
            "Get details about the program, eligibility, curriculum, "
            "training, practical learning, and career opportunities.\n\n"
            "Please choose an option below 👇"
        )
    )

    footer = MessageFooter(
        text="🎓 GM University Admissions 2026-27"
    )

    btn_program_details = Button(reply=ButtonReply(id="agaba", title="Program Details"))
    btn_fee_duration = Button(reply=ButtonReply(id="agabb", title="Fee Details"))
    btn_branch_website = Button(reply=ButtonReply(id="agabc", title="More Info"))

    action = ButtonAction(buttons=[btn_program_details, btn_fee_duration, btn_branch_website])

    interactive = InteractiveButton(
        header=header,
        body=body,
        footer=footer,
        action=action,
    )

    payload = WhatsAppInteractiveButtonRequest(to=wa_id, interactive=interactive)
    return payload.model_dump()


def build_bvoc_fdam_program_details_payload(wa_id: str):
    """Builds a well-formatted WhatsApp text payload for full B.Voc Fashion Design and Apparel Manufacture program details."""

    text = (
        "🎓 *B.Voc in Fashion Design and Apparel Manufacture*\n"
        "📘 *Program Details – 2026-27 Intake*\n\n"

        "━━━━━━━━━━━━━━━\n"
        "📄 *Program Document Includes:*\n"
        "• Curriculum Structure\n"
        "• Eligibility Criteria\n"
        "• Fashion Design Core Subjects\n"
        "• Apparel Manufacture Training\n"
        "• Practical & Industry-Oriented Learning\n"
        "• Academic & Career Opportunities\n"
        "━━━━━━━━━━━━━━━\n\n"

        "🔗 *View Full Program Document:*\n"
        "http://gmu.ac.in/pdfview_assets%5Cdownloadmaterial%5CB%20Voc%20Programs%202026-27%5CB%20Voc%20-%20Program%20Document%20-%202026-27%5CPROGRAM%20DOCUMENT-%20FDAM-FINAL.pdf"

        "\n\n📞 *Contact Details*\n"
        "━━━━━━━━━━━━━━━\n"
        "📍 GM University, Davangere\n"
        "☎️ Phone: +91 9364099712,+91 9364099720\n"
        # "📧 Email: bvoc.fdam@gmu.ac.in\n"
    )

    payload = WhatsAppTextReplyRequest(
        to=wa_id,
        text=TextBody(
            body=text,
            preview_url=True
        ),
    )

    return payload.model_dump()


def build_bvoc_fdam_fee_duration_payload(wa_id: str):
    """Builds a well-formatted WhatsApp text payload for B.Voc Fashion Design and Apparel Manufacture fee information."""

    text = (
        "🎓 *GM University – B.Voc Fashion Design and Apparel Manufacture Fee Details*\n\n"

        "📌 Fee details will be updated by the university admission office.\n\n"

        "📘 *Program Information:*\n"
        "━━━━━━━━━━━━━━━\n"
        "• Skill-based vocational program\n"
        "• Fashion design practical training\n"
        "• Apparel manufacturing techniques\n"
        "• Studio and workshop-based learning\n"
        "• Career opportunities in fashion and apparel sectors\n"
        "━━━━━━━━━━━━━━━\n\n"

        "📞 *Contact Details*\n"
        "━━━━━━━━━━━━━━━\n"
        "📍 GM University, Davangere\n"
        "☎️ Phone: +91 9364099712,+91 9364099720\n"
        # "📧 Email: bvoc.fdam@gmu.ac.in\n"
    )

    payload = WhatsAppTextReplyRequest(
        to=wa_id,
        text=TextBody(
            body=text,
            preview_url=False
        ),
    )

    return payload.model_dump()


def build_bvoc_fdam_branch_website_payload(wa_id: str):
    """Builds a well-formatted WhatsApp text payload for B.Voc Fashion Design and Apparel Manufacture information."""

    text = (
        "👗🧵 *GM University – B.Voc Fashion Design and Apparel Manufacture*\n\n"

        "📌 Official website/link will be updated soon.\n\n"

        "Stay connected with GM University for updates regarding:\n"
        "━━━━━━━━━━━━━━━\n"
        "• Program Overview\n"
        "• Curriculum Details\n"
        "• Practical Training\n"
        "• Fashion Studio Facilities\n"
        "• Apparel Manufacturing Workshops\n"
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
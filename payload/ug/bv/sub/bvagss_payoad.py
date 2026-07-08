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

def build_bvoc_agss_program_payload(wa_id: str):
   
    """Builds the payload for the B.Voc Airport Ground Services and Support program."""

    header = MessageHeader(
        text="✈️🛄 B.Voc Airport Ground Services and Support"
    )

    body = MessageBody(
        text=(
            "🎓 *B.Voc in Airport Ground Services and Support*\n\n"
            "Learn core concepts in:\n"
            "• Airport Operations Management\n"
            "• Passenger Handling Services\n"
            "• Baggage Handling Systems\n"
            "• Aviation Safety and Security\n"
            "• Ground Support Equipment\n"
            "• Cargo and Logistics Management\n"
            "• Airline Customer Service\n"
            "• Airport Communication Systems\n"
            "• Ramp Operations\n"
            "• Aviation Regulations and Procedures\n\n"
            "Get details about the program, eligibility, curriculum, "
            "training, practical learning, and career opportunities.\n\n"
            "Please choose an option below 👇"
        )
    )

    footer = MessageFooter(
        text="🎓 GM University Admissions 2026-27"
    )

    btn_program_details = Button(reply=ButtonReply(id="agada", title="Program Details"))
    btn_fee_duration = Button(reply=ButtonReply(id="agadb", title="Fee Details"))
    btn_branch_website = Button(reply=ButtonReply(id="agadc", title="More Info"))

    action = ButtonAction(buttons=[btn_program_details, btn_fee_duration, btn_branch_website])

    interactive = InteractiveButton(
        header=header,
        body=body,
        footer=footer,
        action=action,
    )

    payload = WhatsAppInteractiveButtonRequest(to=wa_id, interactive=interactive)
    return payload.model_dump()


def build_bvoc_agss_program_details_payload(wa_id: str):
    """Builds a well-formatted WhatsApp text payload for full B.Voc Airport Ground Services and Support program details."""

    text = (
        "🎓 *B.Voc in Airport Ground Services and Support*\n"
        "📘 *Program Details – 2026-27 Intake*\n\n"

        "━━━━━━━━━━━━━━━\n"
        "📄 *Program Document Includes:*\n"
        "• Curriculum Structure\n"
        "• Eligibility Criteria\n"
        "• Airport Ground Services Core Subjects\n"
        "• Aviation Industry Training\n"
        "• Practical & Industry-Oriented Learning\n"
        "• Academic & Career Opportunities\n"
        "━━━━━━━━━━━━━━━\n\n"

        "🔗 *View Full Program Document:*\n"
        "https://gmu.ac.in/pdfview_assets%5Cdownloadmaterial%5CB%20Voc%20Programs%202026-27%5CB%20Voc%20-%20Program%20Document%20-%202026-27%5CPROGRAM%20DOCUMENT-%20AGSS-FINAL.pdf"

        "\n\n📞 *Contact Details*\n"
        "━━━━━━━━━━━━━━━\n"
        "📍 GM University, Davangere\n"
        "☎️ Phone: +91 9364099712,+91 9364099720\n"
        # "📧 Email: bvoc.agss@gmu.ac.in\n"
    )

    payload = WhatsAppTextReplyRequest(
        to=wa_id,
        text=TextBody(
            body=text,
            preview_url=True
        ),
    )

    return payload.model_dump()


def build_bvoc_agss_fee_duration_payload(wa_id: str):
    """Builds a well-formatted WhatsApp text payload for B.Voc Airport Ground Services and Support fee information."""

    text = (
        "🎓 *GM University – B.Voc Airport Ground Services and Support Fee Details*\n\n"

        "📌 Fee details will be updated by the university admission office.\n\n"

        "📘 *Program Information:*\n"
        "━━━━━━━━━━━━━━━\n"
        "• Skill-based vocational program\n"
        "• Airport operations practical training\n"
        "• Ground handling and passenger services\n"
        "• Aviation industry-oriented curriculum\n"
        "• Career opportunities in airports and airlines\n"
        "━━━━━━━━━━━━━━━\n\n"

        "📞 *Contact Details*\n"
        "━━━━━━━━━━━━━━━\n"
        "📍 GM University, Davangere\n"
        "☎️ Phone: +91 9364099712,+91 9364099720\n"
        # "📧 Email: bvoc.agss@gmu.ac.in\n"
    )

    payload = WhatsAppTextReplyRequest(
        to=wa_id,
        text=TextBody(
            body=text,
            preview_url=False
        ),
    )

    return payload.model_dump()


def build_bvoc_agss_branch_website_payload(wa_id: str):
    """Builds a well-formatted WhatsApp text payload for B.Voc Airport Ground Services and Support information."""

    text = (
        "✈️🛄 *GM University – B.Voc Airport Ground Services and Support*\n\n"

        "📌 Official website/link will be updated soon.\n\n"

        "Stay connected with GM University for updates regarding:\n"
        "━━━━━━━━━━━━━━━\n"
        "• Program Overview\n"
        "• Curriculum Details\n"
        "• Practical Training\n"
        "• Aviation Industry Exposure\n"
        "• Airport Operations Training\n"
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
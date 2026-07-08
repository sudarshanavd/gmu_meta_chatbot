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

def build_bvoc_dda_program_payload(wa_id: str):
    """Builds the payload for the B.Voc Drone Development and Application program."""

    header = MessageHeader(
        text="🚁 B.Voc Drone Development and Application"
    )

    body = MessageBody(
        text=(
            "🎓 *B.Voc in Drone Development and Application*\n\n"
            "Learn core concepts in:\n"
            "• Drone Technology Fundamentals\n"
            "• UAV Design and Development\n"
            "• Drone Assembly and Maintenance\n"
            "• Flight Control Systems\n"
            "• Sensors and Embedded Systems\n"
            "• Remote Sensing Applications\n"
            "• Drone Mapping and Surveying\n"
            "• Aerial Photography and Videography\n"
            "• Drone Safety and Regulations\n"
            "• Industrial Drone Applications\n\n"
            "Get details about the program, eligibility, curriculum, "
            "training, practical learning, and career opportunities.\n\n"
            "Please choose an option below 👇"
        )
    )

    footer = MessageFooter(
        text="🎓 GM University Admissions 2026-27"
    )

    btn_program_details = Button(reply=ButtonReply(id="agaca", title="Program Details"))
    btn_fee_duration = Button(reply=ButtonReply(id="agacb", title="Fee Details"))
    btn_branch_website = Button(reply=ButtonReply(id="agacc", title="More Info"))

    action = ButtonAction(buttons=[btn_program_details, btn_fee_duration, btn_branch_website])

    interactive = InteractiveButton(
        header=header,
        body=body,
        footer=footer,
        action=action,
    )

    payload = WhatsAppInteractiveButtonRequest(to=wa_id, interactive=interactive)
    return payload.model_dump()


def build_bvoc_dda_program_details_payload(wa_id: str):
    """Builds a well-formatted WhatsApp text payload for full B.Voc Drone Development and Application program details."""

    text = (
        "🎓 *B.Voc in Drone Development and Application*\n"
        "📘 *Program Details – 2026-27 Intake*\n\n"

        "━━━━━━━━━━━━━━━\n"
        "📄 *Program Document Includes:*\n"
        "• Curriculum Structure\n"
        "• Eligibility Criteria\n"
        "• Drone Technology Core Subjects\n"
        "• UAV Development Training\n"
        "• Practical & Industry-Oriented Learning\n"
        "• Academic & Career Opportunities\n"
        "━━━━━━━━━━━━━━━\n\n"

        "🔗 *View Full Program Document:*\n"
        "https://gmu.ac.in/pdfview_assets%5Cdownloadmaterial%5CB%20Voc%20Programs%202026-27%5CB%20Voc%20-%20Program%20Document%20-%202026-27%5CPROGRAM%20DOCUMENT%20-%20DDA-FINAL.pdf"

        "\n\n📞 *Contact Details*\n"
        "━━━━━━━━━━━━━━━\n"
        "📍 GM University, Davangere\n"
        "☎️ Phone: +91 9364099712,+91 9364099720\n"
        # "📧 Email: bvoc.dda@gmu.ac.in\n"
    )

    payload = WhatsAppTextReplyRequest(
        to=wa_id,
        text=TextBody(
            body=text,
            preview_url=True
        ),
    )

    return payload.model_dump()


def build_bvoc_dda_fee_duration_payload(wa_id: str):
    """Builds a well-formatted WhatsApp text payload for B.Voc Drone Development and Application fee information."""

    text = (
        "🎓 *GM University – B.Voc Drone Development and Application Fee Details*\n\n"

        "📌 Fee details will be updated by the university admission office.\n\n"

        "📘 *Program Information:*\n"
        "━━━━━━━━━━━━━━━\n"
        "• Skill-based vocational program\n"
        "• Drone development practical training\n"
        "• UAV assembly and maintenance\n"
        "• Field-based drone applications\n"
        "• Career opportunities in drone and UAV sectors\n"
        "━━━━━━━━━━━━━━━\n\n"

        "📞 *Contact Details*\n"
        "━━━━━━━━━━━━━━━\n"
        "📍 GM University, Davangere\n"
        "☎️ Phone: +91 9364099712,+91 9364099720\n"
        # "📧 Email: bvoc.dda@gmu.ac.in\n"
    )

    payload = WhatsAppTextReplyRequest(
        to=wa_id,
        text=TextBody(
            body=text,
            preview_url=False
        ),
    )

    return payload.model_dump()


def build_bvoc_dda_branch_website_payload(wa_id: str):
    """Builds a well-formatted WhatsApp text payload for B.Voc Drone Development and Application information."""

    text = (
        "🚁 *GM University – B.Voc Drone Development and Application*\n\n"

        "📌 Official website/link will be updated soon.\n\n"

        "Stay connected with GM University for updates regarding:\n"
        "━━━━━━━━━━━━━━━\n"
        "• Program Overview\n"
        "• Curriculum Details\n"
        "• Practical Training\n"
        "• Drone Lab Facilities\n"
        "• UAV Development Workshops\n"
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
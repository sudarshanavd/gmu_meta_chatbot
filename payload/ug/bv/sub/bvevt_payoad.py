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

def build_bvoc_evt_program_payload(wa_id: str):
    """Builds the payload for the B.Voc Electrical Vehicle Technology program."""

    header = MessageHeader(
        text="🔋🚗 B.Voc Electrical Vehicle Technology"
    )

    body = MessageBody(
        text=(
            "🎓 *B.Voc in Electrical Vehicle Technology*\n\n"
            "Learn core concepts in:\n"
            "• Electric Vehicle Fundamentals\n"
            "• EV Powertrain Systems\n"
            "• Battery Technology\n"
            "• Battery Management Systems\n"
            "• Electric Motors and Drives\n"
            "• Power Electronics\n"
            "• EV Charging Infrastructure\n"
            "• Vehicle Diagnostics\n"
            "• Automobile Electrical Systems\n"
            "• EV Maintenance and Safety\n\n"
            "Get details about the program, eligibility, curriculum, "
            "training, practical learning, and career opportunities.\n\n"
            "Please choose an option below 👇"
        )
    )

    footer = MessageFooter(
        text="🎓 GM University Admissions 2026-27"
    )

    btn_program_details = Button(reply=ButtonReply(id="agaaa", title="Program Details"))
    btn_fee_duration = Button(reply=ButtonReply(id="agaab", title="Fee Details"))
    btn_branch_website = Button(reply=ButtonReply(id="agaac", title="More Info"))

    action = ButtonAction(buttons=[btn_program_details, btn_fee_duration, btn_branch_website])

    interactive = InteractiveButton(
        header=header,
        body=body,
        footer=footer,
        action=action,
    )

    payload = WhatsAppInteractiveButtonRequest(to=wa_id, interactive=interactive)
    return payload.model_dump()


def build_bvoc_evt_program_details_payload(wa_id: str):
    """Builds a well-formatted WhatsApp text payload for full B.Voc Electrical Vehicle Technology program details."""

    text = (
        "🎓 *B.Voc in Electrical Vehicle Technology*\n"
        "📘 *Program Details – 2026-27 Intake*\n\n"

        "━━━━━━━━━━━━━━━\n"
        "📄 *Program Document Includes:*\n"
        "• Curriculum Structure\n"
        "• Eligibility Criteria\n"
        "• EV Technology Core Subjects\n"
        "• Skill-Based Training\n"
        "• Practical & Industry-Oriented Learning\n"
        "• Academic & Career Opportunities\n"
        "━━━━━━━━━━━━━━━\n\n"

        "🔗 *View Full Program Document:*\n"
        "https://gmu.ac.in/pdfview_assets%5Cdownloadmaterial%5CB%20Voc%20Programs%202026-27%5CB%20Voc%20-%20Program%20Document%20-%202026-27%5CPROGRAM%20DOCUMENT-EVT-FINAL.pdf"

        "\n\n📞 *Contact Details*\n"
        "━━━━━━━━━━━━━━━\n"
        "📍 GM University, Davangere\n"
        "☎️ Phone: +91 9364099712,+91 9364099720\n"
        # "📧 Email: bvoc.evt@gmu.ac.in\n"
    )

    payload = WhatsAppTextReplyRequest(
        to=wa_id,
        text=TextBody(
            body=text,
            preview_url=True
        ),
    )

    return payload.model_dump()


def build_bvoc_evt_fee_duration_payload(wa_id: str):
    """Builds a well-formatted WhatsApp text payload for B.Voc Electrical Vehicle Technology fee information."""

    text = (
        "🎓 *GM University – B.Voc Electrical Vehicle Technology Fee Details*\n\n"

        "📌 Fee details will be updated by the university admission office.\n\n"

        "📘 *Program Information:*\n"
        "━━━━━━━━━━━━━━━\n"
        "• Skill-based vocational program\n"
        "• EV technology practical training\n"
        "• Industry-oriented curriculum\n"
        "• Laboratory and workshop-based learning\n"
        "• Career opportunities in EV and automobile sectors\n"
        "━━━━━━━━━━━━━━━\n\n"

        "📞 *Contact Details*\n"
        "━━━━━━━━━━━━━━━\n"
        "📍 GM University, Davangere\n"
        "☎️ Phone: +91 9364099712,+91 9364099720\n"
        # "📧 Email: bvoc.evt@gmu.ac.in\n"
    )

    payload = WhatsAppTextReplyRequest(
        to=wa_id,
        text=TextBody(
            body=text,
            preview_url=False
        ),
    )

    return payload.model_dump()


def build_bvoc_evt_branch_website_payload(wa_id: str):
    """Builds a well-formatted WhatsApp text payload for B.Voc Electrical Vehicle Technology information."""

    text = (
        "🔋🚗 *GM University – B.Voc Electrical Vehicle Technology*\n\n"

        "📌 Official website/link will be updated soon.\n\n"

        "Stay connected with GM University for updates regarding:\n"
        "━━━━━━━━━━━━━━━\n"
        "• Program Overview\n"
        "• Curriculum Details\n"
        "• Practical Training\n"
        "• EV Laboratory Facilities\n"
        "• Industry Skill Development\n"
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
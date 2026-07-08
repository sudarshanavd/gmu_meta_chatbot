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

def build_bt_program_payload(wa_id: str):
    """Builds the payload for the Biotechnology (BT) program."""

    header = MessageHeader(
        text="🧬 Biotechnology (BT)"
    )

    body = MessageBody(
        text=(
            "🎓 *B.Tech in Biotechnology (BT)*\n\n"
            "Learn core concepts in:\n"
            "• Molecular Biology\n"
            "• Genetic Engineering\n"
            "• Microbiology\n"
            "• Biochemistry\n"
            "• Cell Biology\n"
            "• Bioinformatics\n"
            "• Immunology\n"
            "• Bioprocess Engineering\n"
            "• Environmental Biotechnology\n"
            "• Industrial & Medical Biotechnology\n\n"
            "Get details about the program, fee structure, placements, "
            "and department information.\n\n"
            "Please choose an option below 👇"
        )
    )

    footer = MessageFooter(
        text="🎓 GM University Admissions 2026-27"
    )

    btn_program_details = Button(reply=ButtonReply(id="aabfa", title="Program Details"))
    btn_fee_duration = Button(reply=ButtonReply(id="aabfb", title="Fee & Duration"))
    btn_branch_website = Button(reply=ButtonReply(id="aabfc", title="Branch Website"))

    action = ButtonAction(
        buttons=[btn_program_details, btn_fee_duration, btn_branch_website]
    )

    interactive = InteractiveButton(
        header=header,
        body=body,
        footer=footer,
        action=action,
    )

    payload = WhatsAppInteractiveButtonRequest(
        to=wa_id,
        interactive=interactive
    )

    return payload.model_dump()


def build_bt_program_details_payload(wa_id: str):
    """Builds a well-formatted WhatsApp text payload for full Biotechnology program details."""

    text = (
        "🎓 *B.Tech Biotechnology (BT)*\n"
        "📘 *Program Details – 2026-27 Intake*\n\n"

        "━━━━━━━━━━━━━━━\n"
        "📄 *Program Brochure Includes:*\n"
        "• Curriculum Structure\n"
        "• Eligibility Criteria\n"
        "• Core Biotechnology Subjects\n"
        "• Laboratory & Research Facilities\n"
        "• Department Highlights\n"
        "• Academic & Career Opportunities\n"
        "━━━━━━━━━━━━━━━\n\n"

        "🔗 *View Full Program Brochure:*\n"
        "https://gmu.ac.in/pdfview_assets%5Cdownloadmaterial%5CUG%20Programs%5Cprogram%5CPD_BT_2026-27.pdf"

        "\n\n📞 *Contact Details*\n"
        "━━━━━━━━━━━━━━━\n"
        "📍 GM University, Davangere\n"
        "☎️ Phone: +91 9364099712,+91 9364099720\n"
        "📧 Email: hod.bt@gmu.ac.in\n"
    )

    payload = WhatsAppTextReplyRequest(
        to=wa_id,
        text=TextBody(
            body=text,
            preview_url=True
        ),
    )

    return payload.model_dump()


def build_bt_fee_duration_payload(wa_id: str):
    """Builds a well-formatted WhatsApp text payload for Biotechnology fee and duration information."""

    text = (
        "🎓 *GM University – Biotechnology (BT) Program Fee Details*\n\n"

        "🧬 *Current Biotechnology Program Fee*\n"
        "━━━━━━━━━━━━━━━\n"
        "₹1,65,000 per year\n\n"

        "⏳ *Program Duration*\n"
        "━━━━━━━━━━━━━━━\n"
        "4 Years (8 Semesters)\n\n"

        "📞 *Contact Details*\n"
        "━━━━━━━━━━━━━━━\n"
        "📍 GM University, Davangere\n"
        "☎️ Phone: +91 9364099712,+91 9364099720\n"
        "📧 Email: hod.bt@gmu.ac.in\n"
    )

    payload = WhatsAppTextReplyRequest(
        to=wa_id,
        text=TextBody(
            body=text,
            preview_url=True
        ),
    )

    return payload.model_dump()


def build_bt_branch_website_payload(wa_id: str):
    """Builds a well-formatted WhatsApp text payload for the Biotechnology branch website."""

    text = (
        "🧬 *GM University – Biotechnology (BT)*\n\n"

        "🌐 Explore the official Biotechnology department website for:\n"
        "━━━━━━━━━━━━━━━\n"
        "• Department Overview\n"
        "• Programs & Curriculum\n"
        "• Faculty Information\n"
        "• Research & Innovation\n"
        "• Laboratories & Facilities\n"
        "• Events & Activities\n"
        "• Placement Highlights\n"
        "• Student Resources\n"
        "━━━━━━━━━━━━━━━\n\n"

        "🔗 *Visit Website:*\n"
        "https://gmu.ac.in/biotech/"
    )

    payload = WhatsAppTextReplyRequest(
        to=wa_id,
        text=TextBody(
            body=text,
            preview_url=True
        ),
    )

    return payload.model_dump()
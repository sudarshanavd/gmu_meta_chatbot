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

def build_bsc_fst_program_payload(wa_id: str):
    """Builds the payload for the Food Science and Technology program."""

    header = MessageHeader(
        text="🍽️🔬 Food Science and Technology"
    )

    body = MessageBody(
        text=(
            "🎓 *B.Sc Food Science and Technology*\n\n"
            "Learn core concepts in:\n"
            "• Food Chemistry\n"
            "• Food Microbiology\n"
            "• Food Processing Technology\n"
            "• Food Preservation\n"
            "• Food Quality Control\n"
            "• Food Safety & Hygiene\n"
            "• Nutrition Science\n"
            "• Dairy Technology\n"
            "• Packaging Technology\n"
            "• Food Product Development\n\n"
            "Get details about the program, fee structure, placements, "
            "and department information.\n\n"
            "Please choose an option below 👇"
        )
    )

    footer = MessageFooter(
        text="🎓 GM University Admissions 2026-27"
    )

    btn_program_details = Button(reply=ButtonReply(id="adcaa", title="Program Details"))
    btn_fee_duration = Button(reply=ButtonReply(id="adcab", title="Fee & Duration"))
    btn_branch_website = Button(reply=ButtonReply(id="adcac", title="Branch Website"))

    action = ButtonAction(buttons=[btn_program_details, btn_fee_duration, btn_branch_website])

    interactive = InteractiveButton(
        header=header,
        body=body,
        footer=footer,
        action=action,
    )

    payload = WhatsAppInteractiveButtonRequest(to=wa_id, interactive=interactive)
    return payload.model_dump()


def build_bsc_fst_program_details_payload(wa_id: str):
    """Builds a well-formatted WhatsApp text payload for full Food Science and Technology program details."""

    text = (
        "🎓 *B.Sc Food Science and Technology*\n"
        "🏫 *School of Applied Sciences*\n"
        "📘 *Program Details – 2026-27 Intake*\n\n"

        "━━━━━━━━━━━━━━━\n"
        "📄 *Program Brochure Includes:*\n"
        "• Curriculum Structure\n"
        "• Eligibility Criteria\n"
        "• Food Science & Technology Core Subjects\n"
        "• School Highlights\n"
        "• Academic & Career Opportunities\n"
        "━━━━━━━━━━━━━━━\n\n"

        "🔗 *View Full Program Brochure:*\n"
        "https://www.gmu.ac.in/pdfview_assets%5Cdownloadmaterial%5CSchool%20of%20Applied%20Sciences-%20Program%20Docs%5CPD_FST_2026-27.pdf"

        "\n\n📞 *Contact Details*\n"
        "━━━━━━━━━━━━━━━\n"
        "📍 GM University, Davangere\n"
        "☎️ Phone: +91 9364099712,+91 9364099720\n"
        # "📧 Email: bscfst@gmu.ac.in\n"
    )

    payload = WhatsAppTextReplyRequest(
        to=wa_id,
        text=TextBody(
            body=text,
            preview_url=True
        ),
    )

    return payload.model_dump()


def build_bsc_fst_fee_duration_payload(wa_id: str):
    """Builds a well-formatted WhatsApp text payload for Food Science and Technology fee and duration information."""

    text = (
        "🎓 *GM University – Food Science and Technology Program Fee Details*\n\n"

        "🍽️🔬 *Current Food Science and Technology Fee*\n"
        "━━━━━━━━━━━━━━━\n"
        "Program Annual Fee ₹92,500\n\n"

        "⏳ *Program Duration*\n"
        "━━━━━━━━━━━━━━━\n"
        "3 Years \n\n"

        "📞 *Contact Details*\n"
        "━━━━━━━━━━━━━━━\n"
        "📍 GM University, Davangere\n"
        "☎️ Phone: +91 9364099712,+91 9364099720\n"
        # "📧 Email: bscfst@gmu.ac.in\n"
    )

    payload = WhatsAppTextReplyRequest(
        to=wa_id,
        text=TextBody(
            body=text,
            preview_url=False
        ),
    )

    return payload.model_dump()


def build_bsc_fst_branch_website_payload(wa_id: str):
    """Builds a well-formatted WhatsApp text payload for the School of Applied Sciences website."""

    text = (
        "🍽️🔬 *GM University – School of Applied Sciences*\n\n"

        "🌐 Official website will be updated soon.\n\n"

        "📌 Stay connected with GM University for the latest updates regarding:\n"
        "━━━━━━━━━━━━━━━\n"
        "• School Overview\n"
        "• Programs & Curriculum\n"
        "• Faculty Information\n"
        "• Food Science Laboratories\n"
        "• Food Processing Facilities\n"
        "• Events & Seminars\n"
        "• Placement Highlights\n"
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
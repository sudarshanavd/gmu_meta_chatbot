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

def build_ed_program_payload(wa_id: str):
    """Builds the payload for the Engineering Design program."""

    header = MessageHeader(
        text="Engineering Design"
    )

    body = MessageBody(
        text=(
            "🎓 *B.Tech in Engineering Design (ED)*\n\n"
            "Learn core concepts in:\n"
            "• Engineering Graphics\n"
            "• Product Design\n"
            "• Computer Aided Design (CAD)\n"
            "• Manufacturing Processes\n"
            "• Design Thinking\n"
            "• Mechatronics\n"
            "• Industrial Design\n"
            "• Rapid Prototyping\n"
            "• 3D Modeling & Simulation\n"
            "• Product Development\n\n"
            "Get details about the program, fee structure, placements, "
            "and department information.\n\n"
            "Please choose an option below 👇"
        )
    )

    footer = MessageFooter(
        text="🎓 GM University Admissions 2026-27"
    )

    btn_program_details = Button(reply=ButtonReply(id="aabda", title="Program Details"))
    btn_fee_duration = Button(reply=ButtonReply(id="aabdb", title="Fee & Duration"))
    # btn_branch_website = Button(reply=ButtonReply(id="00513", title="Branch Website"))

    action = ButtonAction(
        # buttons=[btn_program_details, btn_fee_duration, btn_branch_website]
        buttons=[btn_program_details, btn_fee_duration]
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


def build_ed_program_details_payload(wa_id: str):
    """Builds a well-formatted WhatsApp text payload for full Engineering Design program details."""

    text = (
        "🎓 *B.Tech Engineering Design (ED)*\n"
        "📘 *Program Details – 2026-27 Intake*\n\n"
        "━━━━━━━━━━━━━━━\n"
        "📄 *Program Brochure Includes:*\n"
        "• Curriculum Structure\n"
        "• Eligibility Criteria\n"
        "• Engineering Design Core Subjects\n"
        "• Department Highlights\n"
        "• Academic & Career Opportunities\n"
        "━━━━━━━━━━━━━━━\n\n"
        "🔗 *View Full Program Brochure:*\n"
        "http://gmu.ac.in/pdfview_assets%5Cdownloadmaterial%5CUG%20Programs%5CPD_ED_2026-27.pdf"
        "\n\n📞 *Contact Details*\n"
        "━━━━━━━━━━━━━━━\n"
        "📍 GM University, Davangere\n"
        "☎️ Phone: +91 9364099712,+91 9364099720\n"
        "📧 Email: hod.ed@gmu.ac.in\n"
    )

    payload = WhatsAppTextReplyRequest(
        to=wa_id,
        text=TextBody(
            body=text,
            preview_url=True
        ),
    )

    return payload.model_dump()


def build_ed_fee_duration_payload(wa_id: str):
    """Builds a well-formatted WhatsApp text payload for Engineering Design fee and duration information."""

    text = (
        "🎓 *GM University – Engineering Design Program Fee Details*\n\n"
        "*Current Engineering Design Fee*\n"
        "━━━━━━━━━━━━━━━\n"
        "₹1,65,000 per year\n\n"
        
        "⏳ *Program Duration*\n"
        "━━━━━━━━━━━━━━━\n"
        "4 Years (8 Semesters)\n\n"
        
        "📞 *Contact Details*\n"
        "━━━━━━━━━━━━━━━\n"
        "📍 GM University, Davangere\n"
        "☎️ Phone: +91 9364099712,+91 9364099720\n"
        "📧 Email: hod.ed@gmu.ac.in\n"
    )

    payload = WhatsAppTextReplyRequest(
        to=wa_id,
        text=TextBody(
            body=text,
            preview_url=True
        ),
    )

    return payload.model_dump()


def build_ed_branch_website_payload(wa_id: str):
    """Builds a well-formatted WhatsApp text payload for the Engineering Design branch website."""

    text = (
        "*GM University – Engineering Design*\n\n"
        "🌐 Explore the official Engineering Design website for:\n"
        "━━━━━━━━━━━━━━━\n"
        "• Department Overview\n"
        "• Programs & Curriculum\n"
        "• Faculty Information\n"
        "• Design Studios & CAD Labs\n"
        "• Events & Activities\n"
        "• Placement Highlights\n"
        "• Student Resources\n"
        "━━━━━━━━━━━━━━━\n\n"
        "🔗 *Visit Website:*\n"
        "https://ra-gmu.netlify.app/"
    )

    payload = WhatsAppTextReplyRequest(
        to=wa_id,
        text=TextBody(
            body=text,
            preview_url=True
        ),
    )

    return payload.model_dump()
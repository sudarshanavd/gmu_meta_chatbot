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

def build_bcom_general_program_payload(wa_id: str):
    """Builds the payload for the B.Com (General) program."""

    header = MessageHeader(
        text="📘 B.Com (General)"
    )

    body = MessageBody(
        text=(
            "🎓 *Bachelor of Commerce (B.Com - General)*\n\n"
            "Learn core concepts in:\n"
            "• Financial Accounting\n"
            "• Business Economics\n"
            "• Business Law\n"
            "• Corporate Accounting\n"
            "• Cost Accounting\n"
            "• Income Tax\n"
            "• Auditing\n"
            "• Financial Management\n"
            "• Marketing Management\n"
            "• Entrepreneurship Development\n\n"
            "Get details about the program, fee structure, placements, "
            "and department information.\n\n"
            "Please choose an option below 👇"
        )
    )

    footer = MessageFooter(
        text="🎓 GM University Admissions 2026-27"
    )

    btn_program_details = Button(
        reply=ButtonReply(id="abaaa", title="Program Details")
    )
    btn_fee_duration = Button(
        reply=ButtonReply(id="abaab", title="Fee & Duration")
    )
    btn_branch_website = Button(
        reply=ButtonReply(id="abaac", title="Branch Website")
    )

    action = ButtonAction(
        buttons=[
            btn_program_details,
            btn_fee_duration,
            btn_branch_website,
        ]
    )

    interactive = InteractiveButton(
        header=header,
        body=body,
        footer=footer,
        action=action,
    )

    payload = WhatsAppInteractiveButtonRequest(
        to=wa_id,
        interactive=interactive,
    )

    return payload.model_dump()

def build_bcom_general_program_details_payload(wa_id: str):
    """Builds a well-formatted WhatsApp text payload for the B.Com (General) program details."""

    text = (
        "🎓 *Bachelor of Commerce (B.Com - General)*\n"
        "📘 *Program Details – 2026-27 Intake*\n\n"

        "━━━━━━━━━━━━━━━\n"
        "📄 *Program Brochure Includes:*\n"
        "• Curriculum Structure\n"
        "• Eligibility Criteria\n"
        "• Core Commerce Subjects\n"
        "• Department Highlights\n"
        "• Academic & Career Opportunities\n"
        "• Industry-Oriented Learning\n"
        "━━━━━━━━━━━━━━━\n\n"

        "🔗 *View Full Program Brochure:*\n"
        "https://gmu.ac.in/pdfview_assets%5Cdownloadmaterial%5Cschoolofcommerce%5CPD_%20BCom_2026-27.pdf"

        "\n\n📞 *Contact Details*\n"
        "━━━━━━━━━━━━━━━\n"
        "📍 GM University, Davangere\n"
        "☎️ Phone: +91 9364099712,+91 9364099720\n"
        # "📧 Email: commerce@gmu.ac.in\n"
    )

    payload = WhatsAppTextReplyRequest(
        to=wa_id,
        text=TextBody(
            body=text,
            preview_url=True
        ),
    )

    return payload.model_dump()

def build_bcom_general_fee_duration_payload(wa_id: str):
    """Builds a well-formatted WhatsApp text payload for B.Com (General) fee and duration information."""

    text = (
        "🎓 *GM University – B.Com (General) Fee Details*\n\n"

        "📚 *Current Program Fee*\n"
        "━━━━━━━━━━━━━━━\n"
        "72,500 per year\n\n"

        "⏳ *Program Duration*\n"
        "━━━━━━━━━━━━━━━\n"
        "3 Years \n\n"


        "📞 *Contact Details*\n"
        "━━━━━━━━━━━━━━━\n"
        "📍 GM University, Davangere\n"
        "☎️ Phone: +91 9364099712,+91 9364099720\n"
        # "📧 Email: commerce@gmu.ac.in\n"
    )

    payload = WhatsAppTextReplyRequest(
        to=wa_id,
        text=TextBody(
            body=text,
            preview_url=True
        ),
    )

    return payload.model_dump()

def build_bcom_general_branch_website_payload(wa_id: str):
    """Builds a well-formatted WhatsApp text payload for the B.Com (General) branch website."""

    text = (
        "📘 *GM University – B.Com (General)*\n\n"

        "🌐 Explore the official Faculty of Commerce and Management website for:\n"
        "━━━━━━━━━━━━━━━\n"
        "• Department Overview\n"
        "• Programs Offered\n"
        "• Curriculum Structure\n"
        "• Faculty Information\n"
        "• Academic Activities\n"
        "• Placement & Career Support\n"
        "• Student Resources\n"
        "━━━━━━━━━━━━━━━\n\n"

        "🔗 *Visit Website:*\n"
        "https://faculty-of-commerce-and-management.web.app/"
    )

    payload = WhatsAppTextReplyRequest(
        to=wa_id,
        text=TextBody(
            body=text,
            preview_url=True
        ),
    )

    return payload.model_dump()
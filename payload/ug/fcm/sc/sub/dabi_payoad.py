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

def build_dabi_program_payload(wa_id: str):
    """Builds the payload for the Data Analytics and Business Intelligence program."""

    header = MessageHeader(
        text="📊 Data Analytics and Business Intelligence"
    )

    body = MessageBody(
        text=(
            "🎓 *B.COM in Data Analytics and Business Intelligence (DABI)*\n\n"
            "Learn core concepts in:\n"
            "• Data Analytics\n"
            "• Business Intelligence\n"
            "• Data Visualization\n"
            "• Database Management Systems\n"
            "Get details about the program, fee structure, placements, "
            "and department information.\n\n"
            "Please choose an option below 👇"
        )
    )

    footer = MessageFooter(
        text="🎓 GM University Admissions 2026-27"
    )

    btn_program_details = Button(reply=ButtonReply(id="ababa", title="Program Details"))
    btn_fee_duration = Button(reply=ButtonReply(id="ababb", title="Fee & Duration"))
    btn_branch_website = Button(reply=ButtonReply(id="ababc", title="Branch Website"))

    action = ButtonAction(buttons=[btn_program_details, btn_fee_duration, btn_branch_website])

    interactive = InteractiveButton(
        header=header,
        body=body,
        footer=footer,
        action=action,
    )

    payload = WhatsAppInteractiveButtonRequest(to=wa_id, interactive=interactive)
    return payload.model_dump()


def build_dabi_program_details_payload(wa_id: str):
    """Builds a well-formatted WhatsApp text payload for full DABI program details."""

    text = (
        "🎓 *B.COM Data Analytics and Business Intelligence (DABI)*\n"
        "📘 *Program Details – 2026-27 Intake*\n\n"

        "━━━━━━━━━━━━━━━\n"
        "📄 *Program Brochure Includes:*\n"
        "• Curriculum Structure\n"
        "• Eligibility Criteria\n"
        "• Data Analytics & Business Intelligence Core Subjects\n"
        "• Department Highlights\n"
        "• Academic & Career Opportunities\n"
        "━━━━━━━━━━━━━━━\n\n"

        "🔗 *View Full Program Brochure:*\n"
        "Brochure will be updated soon.\n\n"

        "📞 *Contact Details*\n"
        "━━━━━━━━━━━━━━━\n"
        "📍 GM University, Davangere\n"
        "☎️ Phone: +91 9364099712,+91 9364099720\n"
        # "📧 Email: dabi@gmu.ac.in\n"
    )

    payload = WhatsAppTextReplyRequest(
        to=wa_id,
        text=TextBody(
            body=text,
            preview_url=False
        ),
    )

    return payload.model_dump()


def build_dabi_fee_duration_payload(wa_id: str):
    """Builds a well-formatted WhatsApp text payload for DABI fee and duration information."""

    text = (
        "🎓 *GM University – Data Analytics and Business Intelligence Program Fee Details*\n\n"

        "📊 *Current DABI Fee*\n"
        "━━━━━━━━━━━━━━━\n"
        "₹72,500 per year\n\n"

        "⏳ *Program Duration*\n"
        "━━━━━━━━━━━━━━━\n"
        "3 Years \n\n"

        "📞 *Contact Details*\n"
        "━━━━━━━━━━━━━━━\n"
        "📍 GM University, Davangere\n"
        "☎️ Phone: +91 9364099712,+91 9364099720\n"
        # "📧 Email: dabi@gmu.ac.in\n"
    )

    payload = WhatsAppTextReplyRequest(
        to=wa_id,
        text=TextBody(
            body=text,
            preview_url=True
        ),
    )

    return payload.model_dump()


def build_dabi_branch_website_payload(wa_id: str):
    """Builds a well-formatted WhatsApp text payload for the DABI branch website."""

    text = (
        "📊 *GM University – Data Analytics and Business Intelligence*\n\n"

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
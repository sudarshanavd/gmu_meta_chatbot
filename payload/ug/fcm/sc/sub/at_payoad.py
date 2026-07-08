
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

def build_at_program_payload(wa_id: str):
    """Builds the payload for the Accounting and Taxation program."""

    header = MessageHeader(
        text="💰 Accounting and Taxation"
    )

    body = MessageBody(
        text=(
            "🎓 *B.COM in Accounting and Taxation (AT)*\n\n"
            "Learn core concepts in:\n"
            "• Financial Accounting\n"
            "• Cost Accounting\n"
            "• Corporate Accounting\n"
            "• Direct Taxation\n"
            "• Indirect Taxation (GST)\n"
            "• Auditing\n"
            "• Financial Management\n"
            "• Business Law\n"
            "• Accounting Information Systems\n"
            "• Tax Planning & Compliance\n\n"
            "Get details about the program, fee structure, placements, "
            "and department information.\n\n"
            "Please choose an option below 👇"
        )
    )

    footer = MessageFooter(
        text="🎓 GM University Admissions 2026-27"
    )

    btn_program_details = Button(reply=ButtonReply(id="abada", title="Program Details"))
    btn_fee_duration = Button(reply=ButtonReply(id="abadb", title="Fee & Duration"))
    btn_branch_website = Button(reply=ButtonReply(id="abadc", title="Branch Website"))

    action = ButtonAction(buttons=[btn_program_details, btn_fee_duration, btn_branch_website])

    interactive = InteractiveButton(
        header=header,
        body=body,
        footer=footer,
        action=action,
    )

    payload = WhatsAppInteractiveButtonRequest(to=wa_id, interactive=interactive)
    return payload.model_dump()


def build_at_program_details_payload(wa_id: str):
    """Builds a well-formatted WhatsApp text payload for full AT program details."""

    text = (
        "🎓 *B.COM Accounting and Taxation (AT)*\n"
        "📘 *Program Details – 2026-27 Intake*\n\n"

        "━━━━━━━━━━━━━━━\n"
        "📄 *Program Brochure Includes:*\n"
        "• Curriculum Structure\n"
        "• Eligibility Criteria\n"
        "• Accounting & Taxation Core Subjects\n"
        "• Department Highlights\n"
        "• Academic & Career Opportunities\n"
        "━━━━━━━━━━━━━━━\n\n"

        "🔗 *View Full Program Brochure:*\n"
        "Brochure will be updated soon.\n\n"

        "📞 *Contact Details*\n"
        "━━━━━━━━━━━━━━━\n"
        "📍 GM University, Davangere\n"
        "☎️ Phone: +91 9364099712,+91 9364099720\n"
        # "📧 Email: at@gmu.ac.in\n"
    )

    payload = WhatsAppTextReplyRequest(
        to=wa_id,
        text=TextBody(
            body=text,
            preview_url=False
        ),
    )

    return payload.model_dump()


def build_at_fee_duration_payload(wa_id: str):
    """Builds a well-formatted WhatsApp text payload for AT fee and duration information."""

    text = (
        "🎓 *GM University – Accounting and Taxation Program Fee Details*\n\n"

        "💰 *Current AT Fee*\n"
        "━━━━━━━━━━━━━━━\n"
        "₹72,500 per year\n\n"

        "⏳ *Program Duration*\n"
        "━━━━━━━━━━━━━━━\n"
        "3 Years \n\n"

        "📞 *Contact Details*\n"
        "━━━━━━━━━━━━━━━\n"
        "📍 GM University, Davangere\n"
        "☎️ Phone: +91 9364099712,+91 9364099720\n"
        # "📧 Email: at@gmu.ac.in\n"
    )

    payload = WhatsAppTextReplyRequest(
        to=wa_id,
        text=TextBody(
            body=text,
            preview_url=False
        ),
    )

    return payload.model_dump()


def build_at_branch_website_payload(wa_id: str):
    """Builds a well-formatted WhatsApp text payload for the AT branch website."""

    text = (
        "💰 *GM University – Accounting and Taxation*\n\n"

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



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

def build_bf_program_payload(wa_id: str):
    """Builds the payload for the Blockchain and FinTech program."""

    header = MessageHeader(
        text="⛓️💳 Blockchain and FinTech"
    )

    body = MessageBody(
        text=(
            "🎓 *BBA in Blockchain and FinTech (BF)*\n\n"
            "Learn core concepts in:\n"
            "• Blockchain Fundamentals\n"
            "• Cryptocurrency Technologies\n"
            "• Smart Contracts\n"
            "• Decentralized Finance (DeFi)\n"
            "Get details about the program, fee structure, placements, "
            "and department information.\n\n"
            "Please choose an option below 👇"
        )
    )

    footer = MessageFooter(
        text="🎓 GM University Admissions 2026-27"
    )

    btn_program_details = Button(reply=ButtonReply(id="abbba", title="Program Details"))
    btn_fee_duration = Button(reply=ButtonReply(id="abbbb", title="Fee & Duration"))
    btn_branch_website = Button(reply=ButtonReply(id="abbbc", title="Branch Website"))

    action = ButtonAction(buttons=[btn_program_details, btn_fee_duration, btn_branch_website])

    interactive = InteractiveButton(
        header=header,
        body=body,
        footer=footer,
        action=action,
    )

    payload = WhatsAppInteractiveButtonRequest(to=wa_id, interactive=interactive)
    return payload.model_dump()


def build_bf_program_details_payload(wa_id: str):
    """Builds a well-formatted WhatsApp text payload for full BF program details."""

    text = (
        "🎓 *BBA Blockchain and FinTech (BF)*\n"
        "📘 *Program Details – 2026-27 Intake*\n\n"

        "━━━━━━━━━━━━━━━\n"
        "📄 *Program Brochure Includes:*\n"
        "• Curriculum Structure\n"
        "• Eligibility Criteria\n"
        "• Blockchain & FinTech Core Subjects\n"
        "• Department Highlights\n"
        "• Academic & Career Opportunities\n"
        "━━━━━━━━━━━━━━━\n\n"

        "🔗 *View Full Program Brochure:*\n"
        "Brochure will be updated soon.\n\n"

        "📞 *Contact Details*\n"
        "━━━━━━━━━━━━━━━\n"
        "📍 GM University, Davangere\n"
        "☎️ Phone: +91 9364099712,+91 9364099720\n"
        # "📧 Email: bf@gmu.ac.in\n"
    )

    payload = WhatsAppTextReplyRequest(
        to=wa_id,
        text=TextBody(
            body=text,
            preview_url=False
        ),
    )

    return payload.model_dump()


def build_bf_fee_duration_payload(wa_id: str):
    """Builds a well-formatted WhatsApp text payload for BF fee and duration information."""

    text = (
        "🎓 *GM University – Blockchain and FinTech Program Fee Details*\n\n"

        "⛓️💳 *Current Blockchain and FinTech Fee*\n"
        "━━━━━━━━━━━━━━━\n"
        "₹62,500 Program Annual Fee\n\n"

        "⏳ *Program Duration*\n"
        "━━━━━━━━━━━━━━━\n"
        "3 Years \n\n"

        "📞 *Contact Details*\n"
        "━━━━━━━━━━━━━━━\n"
        "📍 GM University, Davangere\n"
        "☎️ Phone: +91 9364099712,+91 9364099720\n"
        # "📧 Email: bf@gmu.ac.in\n"
    )

    payload = WhatsAppTextReplyRequest(
        to=wa_id,
        text=TextBody(
            body=text,
            preview_url=False
        ),
    )

    return payload.model_dump()


def build_bf_branch_website_payload(wa_id: str):
    """Builds a well-formatted WhatsApp text payload for the BF branch website."""

    text = (
        "⛓️💳 *GM University – Blockchain and FinTech*\n\n"

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
            preview_url=False
        ),
    )

    return payload.model_dump()


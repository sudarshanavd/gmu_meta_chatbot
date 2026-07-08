
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

def build_them_program_payload(wa_id: str):
    """Builds the payload for the Tourism, Hospitality and Event Management program."""

    header = MessageHeader(
        text="🌍🏨 Tourism, Hospitality and Event Management"
    )

    body = MessageBody(
        text=(
            "🎓 *BBA in Tourism, Hospitality and Event Management (THEM)*\n\n"
            "Learn core concepts in:\n"
            "• Tourism Management\n"
            "• Hospitality Management\n"
            "• Event Planning & Management\n"
            "• Travel Agency Operations\n"
            "• Hotel Operations\n"
            "Please choose an option below 👇"
        )
    )

    footer = MessageFooter(
        text="🎓 GM University Admissions 2026-27"
    )

    btn_program_details = Button(reply=ButtonReply(id="abbfa", title="Program Details"))
    btn_fee_duration = Button(reply=ButtonReply(id="abbfb", title="Fee & Duration"))
    btn_branch_website = Button(reply=ButtonReply(id="abbfc", title="Branch Website"))

    action = ButtonAction(buttons=[btn_program_details, btn_fee_duration, btn_branch_website])

    interactive = InteractiveButton(
        header=header,
        body=body,
        footer=footer,
        action=action,
    )

    payload = WhatsAppInteractiveButtonRequest(to=wa_id, interactive=interactive)
    return payload.model_dump()


def build_them_program_details_payload(wa_id: str):
    """Builds a well-formatted WhatsApp text payload for full THEM program details."""

    text = (
        "🎓 *BBA Tourism, Hospitality and Event Management (THEM)*\n"
        "📘 *Program Details – 2026-27 Intake*\n\n"

        "━━━━━━━━━━━━━━━\n"
        "📄 *Program Brochure Includes:*\n"
        "• Curriculum Structure\n"
        "• Eligibility Criteria\n"
        "• Tourism, Hospitality & Event Management Core Subjects\n"
        "• Department Highlights\n"
        "• Academic & Career Opportunities\n"
        "━━━━━━━━━━━━━━━\n\n"

        "🔗 *View Full Program Brochure:*\n"
        "Brochure will be updated soon.\n\n"

        "📞 *Contact Details*\n"
        "━━━━━━━━━━━━━━━\n"
        "📍 GM University, Davangere\n"
        "☎️ Phone: +91 9364099712,+91 9364099720\n"
        # "📧 Email: them@gmu.ac.in\n"
    )

    payload = WhatsAppTextReplyRequest(
        to=wa_id,
        text=TextBody(
            body=text,
            preview_url=False
        ),
    )

    return payload.model_dump()


def build_them_fee_duration_payload(wa_id: str):
    """Builds a well-formatted WhatsApp text payload for THEM fee and duration information."""

    text = (
        "🎓 *GM University – Tourism, Hospitality and Event Management Program Fee Details*\n\n"

        "🌍🏨 *Current THEM Fee*\n"
        "━━━━━━━━━━━━━━━\n"
        "₹72,500 per year\n\n"

        "📞 *Contact Details*\n"
        "━━━━━━━━━━━━━━━\n"
        "📍 GM University, Davangere\n"
        "☎️ Phone: +91 9364099712,+91 9364099720\n"
        # "📧 Email: them@gmu.ac.in\n"
    )

    payload = WhatsAppTextReplyRequest(
        to=wa_id,
        text=TextBody(
            body=text,
            preview_url=False
        ),
    )

    return payload.model_dump()


def build_them_branch_website_payload(wa_id: str):
    """Builds a well-formatted WhatsApp text payload for the THEM branch website."""

    text = (
        "🌍🏨 *GM University – Tourism, Hospitality and Event Management*\n\n"

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

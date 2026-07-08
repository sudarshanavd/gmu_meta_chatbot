
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

def build_aba_program_payload(wa_id: str):
    """Builds the payload for the AI and Business Analytics program."""

    header = MessageHeader(
        text="🤖📈 AI and Business Analytics"
    )

    body = MessageBody(
        text=(
            "🎓 *BBA in AI and Business Analytics (ABA)*\n\n"
            "Learn core concepts in:\n"
            "• Artificial Intelligence\n"
            "• Machine Learning\n"
            "• Business Analytics\n"
            "• Data Science\n"
            "• Data Visualization\n"
            "• Predictive Analytics\n"
            "• Business Intelligence\n"
            "• Statistical Analysis\n"
            "• Decision Support Systems\n"
            "• AI-Driven Business Solutions\n\n"
            "Get details about the program, fee structure, placements, "
            "and department information.\n\n"
            "Please choose an option below 👇"
        )
    )

    footer = MessageFooter(
        text="🎓 GM University Admissions 2026-27"
    )

    btn_program_details = Button(reply=ButtonReply(id="abbca", title="Program Details"))
    btn_fee_duration = Button(reply=ButtonReply(id="abbcb", title="Fee & Duration"))
    btn_branch_website = Button(reply=ButtonReply(id="abbcc", title="Branch Website"))

    action = ButtonAction(buttons=[btn_program_details, btn_fee_duration, btn_branch_website])

    interactive = InteractiveButton(
        header=header,
        body=body,
        footer=footer,
        action=action,
    )

    payload = WhatsAppInteractiveButtonRequest(to=wa_id, interactive=interactive)
    return payload.model_dump()


def build_aba_program_details_payload(wa_id: str):
    """Builds a well-formatted WhatsApp text payload for full ABA program details."""

    text = (
        "🎓 *BBA AI and Business Analytics (ABA)*\n"
        "📘 *Program Details – 2026-27 Intake*\n\n"

        "━━━━━━━━━━━━━━━\n"
        "📄 *Program Brochure Includes:*\n"
        "• Curriculum Structure\n"
        "• Eligibility Criteria\n"
        "• AI & Business Analytics Core Subjects\n"
        "• Department Highlights\n"
        "• Academic & Career Opportunities\n"
        "━━━━━━━━━━━━━━━\n\n"

        "🔗 *View Full Program Brochure:*\n"
        "Brochure will be updated soon.\n\n"

        "📞 *Contact Details*\n"
        "━━━━━━━━━━━━━━━\n"
        "📍 GM University, Davangere\n"
        "☎️ Phone: +91 9364099712,+91 9364099720\n"
        # "📧 Email: aba@gmu.ac.in\n"
    )

    payload = WhatsAppTextReplyRequest(
        to=wa_id,
        text=TextBody(
            body=text,
            preview_url=False
        ),
    )

    return payload.model_dump()


def build_aba_fee_duration_payload(wa_id: str):
    """Builds a well-formatted WhatsApp text payload for ABA fee and duration information."""

    text = (
        "🎓 *GM University – AI and Business Analytics Program Fee Details*\n\n"

        "🤖📈 *Current ABA Fee*\n"
        "━━━━━━━━━━━━━━━\n"
        "Program Annual Fee ₹62,500\n\n"

        "⏳ *Program Duration*\n"
        "━━━━━━━━━━━━━━━\n"
        "3 Years \n\n"

        "💳 *Fee Payment Schedule*\n"
        "━━━━━━━━━━━━━━━\n"

        "📞 *Contact Details*\n"
        "━━━━━━━━━━━━━━━\n"
        "📍 GM University, Davangere\n"
        "☎️ Phone: +91 9364099712,+91 9364099720\n"
        # "📧 Email: aba@gmu.ac.in\n"
    )

    payload = WhatsAppTextReplyRequest(
        to=wa_id,
        text=TextBody(
            body=text,
            preview_url=True
        ),
    )

    return payload.model_dump()


def build_aba_branch_website_payload(wa_id: str):
    """Builds a well-formatted WhatsApp text payload for the ABA branch website."""

    text = (
        "🤖📈 *GM University – AI and Business Analytics*\n\n"

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
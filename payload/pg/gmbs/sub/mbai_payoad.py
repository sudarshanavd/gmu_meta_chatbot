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

def build_mba_international_program_payload(wa_id: str):
    """Builds the payload for the MBA International program."""

    header = MessageHeader(
        text="🌍📈 MBA International"
    )

    body = MessageBody(
        text=(
            "🎓 *MBA International*\n\n"
            "Learn core concepts in:\n"
            "• International Business Management\n"
            "• Global Marketing\n"
            "• International Finance\n"
            "• Cross-Cultural Management\n"
            "• Global Supply Chain Management\n"
            "• Business Analytics\n"
            "• International Trade and Economics\n"
            "• Strategic Management\n"
            "• Entrepreneurship and Innovation\n"
            "• Global Leadership\n\n"
            "Get details about the program, eligibility, curriculum, "
            "international exposure, industry learning, and career opportunities.\n\n"
            "Please choose an option below 👇"
        )
    )

    footer = MessageFooter(
        text="🎓 GM University Admissions 2026-27"
    )

    action = ButtonAction(
        buttons=[
            Button(reply=ButtonReply(id="beada", title="Program Details")),
            Button(reply=ButtonReply(id="beadb", title="Fee Details")),
            Button(reply=ButtonReply(id="beadc", title="More Info")),
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
        interactive=interactive
    )

    return payload.model_dump()


def build_mba_international_program_details_payload(wa_id: str):
    """Builds a WhatsApp text payload for MBA International program details."""

    text = (
        "🎓 *MBA International*\n"
        "📘 *Program Details – 2026-27 Intake*\n\n"
        "━━━━━━━━━━━━━━━\n"
        "📄 *Program Details Include:*\n"
        "• Curriculum Structure\n"
        "• Eligibility Criteria\n"
        "• International Business Subjects\n"
        "• Global Leadership and Strategy Concepts\n"
        "• International Industry Exposure\n"
        "• Practical & Project-Based Training\n"
        "• Career Opportunities\n"
        "━━━━━━━━━━━━━━━\n\n"
        "📞 *Contact Details*\n"
        "━━━━━━━━━━━━━━━\n"
        "📍 GM University, Davangere\n"
        "☎️ Phone: +91 9364099712,+91 9364099720\n"
        # "📧 Email: info@gmu.ac.in"
    )

    payload = WhatsAppTextReplyRequest(
        to=wa_id,
        text=TextBody(
            body=text,
            preview_url=False
        ),
    )

    return payload.model_dump()


def build_mba_international_fee_duration_payload(wa_id: str):
    """Builds a WhatsApp text payload for MBA International fee information."""

    text = (
        "🎓 *GM University – MBA International Fee Details*\n\n"
        "⏱ *Duration:* 2 Years\n"
        "💰 *Program Annual Fee:* ₹2,50,000\n\n"
        "📘 *Program Information:*\n"
        "━━━━━━━━━━━━━━━\n"
        "• International business-focused postgraduate management program\n"
        "• Strong foundation in global business, finance, and leadership\n"
        "• International exposure and cross-cultural learning\n"
        "• Industry-oriented practical training and internships\n"
        "• Career opportunities in multinational companies, global consulting, international trade, and business leadership roles\n"
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


def build_mba_international_branch_website_payload(wa_id: str):
    """Builds a WhatsApp text payload for MBA International information."""

    text = (
        "🌍📈 *GM University – MBA International*\n\n"
        "📌 Official program link will be updated soon.\n\n"
        "Stay connected with GM University for updates regarding:\n"
        "━━━━━━━━━━━━━━━\n"
        "• Program Overview\n"
        "• Curriculum Details\n"
        "• International Exposure\n"
        "• Global Leadership Development\n"
        "• Industry Projects\n"
        "• Placement Opportunities\n"
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


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


def build_mcom_afdb_program_payload(wa_id: str):
    """Builds the payload for the M.Com Applied Finance and Digital Business program."""

    header = MessageHeader(
        text="💰📊 M.Com Applied Finance and Digital Business"
    )

    body = MessageBody(
        text=(
            "🎓 *M.Com in Applied Finance and Digital Business*\n\n"
            "Learn core concepts in:\n"
            "• Applied Finance\n"
            "• Financial Accounting\n"
            "• Corporate Finance\n"
            "• Investment Management\n"
            "• Digital Business\n"
            "• FinTech Applications\n"
            "• Business Analytics\n"
            "• Digital Marketing\n"
            "• Banking and Insurance\n"
            "• Research Methodology\n\n"
            "Get details about the program, eligibility, curriculum, "
            "practical learning, industry training, and career opportunities.\n\n"
            "Please choose an option below 👇"
        )
    )

    footer = MessageFooter(
        text="🎓 GM University Admissions 2026-27"
    )

    btn_program_details = Button(reply=ButtonReply(id="bdaaa", title="Program Details"))
    btn_fee_duration = Button(reply=ButtonReply(id="bdaab", title="Fee Details"))
    btn_branch_website = Button(reply=ButtonReply(id="bdaac", title="More Info"))

    action = ButtonAction(buttons=[btn_program_details, btn_fee_duration, btn_branch_website])

    interactive = InteractiveButton(
        header=header,
        body=body,
        footer=footer,
        action=action,
    )

    payload = WhatsAppInteractiveButtonRequest(to=wa_id, interactive=interactive)
    return payload.model_dump()


def build_mcom_afdb_program_details_payload(wa_id: str):
    """Builds a WhatsApp text payload for M.Com Applied Finance and Digital Business program details."""

    text = (
        "🎓 *M.Com in Applied Finance and Digital Business*\n"
        "📘 *Program Details – 2026-27 Intake*\n\n"

        "━━━━━━━━━━━━━━━\n"
        "📄 *Program Document Includes:*\n"
        "• Curriculum Structure\n"
        "• Eligibility Criteria\n"
        "• Applied Finance Core Subjects\n"
        "• Digital Business and FinTech Concepts\n"
        "• Accounting, Banking and Investment Learning\n"
        "• Practical & Industry-Oriented Training\n"
        "• Career Opportunities\n"
        "━━━━━━━━━━━━━━━\n\n"

        "🔗 *View Full Program Document:*\n"
        "https://gmu.ac.in/pdfview_assets%5Cdownloadmaterial%5Cschoolofcommerce%5CMCom%20Program%20Document%202025-26.pdf"

        "📞 *Contact Details*\n"
        "━━━━━━━━━━━━━━━\n"
        "📍 GM University, Davangere\n"
        "☎️ Phone: +91 9364099712,+91 9364099720\n"
        # "📧 Email: info@gmu.ac.in\n"
    )

    payload = WhatsAppTextReplyRequest(
        to=wa_id,
        text=TextBody(
            body=text,
            preview_url=True
        ),
    )

    return payload.model_dump()


def build_mcom_afdb_fee_duration_payload(wa_id: str):
    """Builds a WhatsApp text payload for M.Com Applied Finance and Digital Business fee information."""

    text = (
        "🎓 *GM University – M.Com Applied Finance and Digital Business Fee Details*\n\n"

        "⏱ *Duration:* 2 Years\n"
        "💰 *Program Annual Fee:* ₹52,500\n\n"

        "📘 *Program Information:*\n"
        "━━━━━━━━━━━━━━━\n"
        "• Applied finance and digital business focused postgraduate program\n"
        "• Strong foundation in accounting, finance, banking and investment\n"
        "• Digital business, FinTech and analytics-based learning\n"
        "• Industry-oriented practical training\n"
        "• Career opportunities in finance, banking, accounting, digital business, FinTech and corporate sectors\n"
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


def build_mcom_afdb_branch_website_payload(wa_id: str):
    """Builds a WhatsApp text payload for M.Com Applied Finance and Digital Business information."""

    text = (
        "💰📊 *GM University – M.Com Applied Finance and Digital Business*\n\n"

        "🔗 *Official Program Document:*\n"
        "https://gmu.ac.in/pdfview_assets%5Cdownloadmaterial%5Cschoolofcommerce%5CMCom%20Program%20Document%202025-26.pdf"
        "Stay connected with GM University for updates regarding:\n"
        "━━━━━━━━━━━━━━━\n"
        "• Program Overview\n"
        "• Curriculum Details\n"
        "• Applied Finance Training\n"
        "• Digital Business Learning\n"
        "• Industry Projects\n"
        "• Placement Opportunities\n"
        "• Student Resources\n"
        "━━━━━━━━━━━━━━━"
    )

    payload = WhatsAppTextReplyRequest(
        to=wa_id,
        text=TextBody(
            body=text,
            preview_url=True
        ),
    )

    return payload.model_dump()
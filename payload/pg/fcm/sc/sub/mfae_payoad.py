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


def build_mcom_fae_program_payload(wa_id: str):
    """Builds the payload for the M.Com Fintech Analytics and Entrepreneurship program."""

    header = MessageHeader(
        text="💳📈 M.Com Fintech Analytics and Entrepreneurship"
    )

    body = MessageBody(
        text=(
            "🎓 *M.Com in Fintech Analytics and Entrepreneurship*\n\n"
            "Learn core concepts in:\n"
            "• Financial Technology\n"
            "• Fintech Analytics\n"
            "• Entrepreneurship Development\n"
            "• Business Analytics\n"
            "• Digital Finance\n"
            "• Investment Management\n"
            "• Banking Technology\n"
            "• Financial Markets\n"
            "• Startup Management\n"
            "• Research Methodology\n\n"
            "Get details about the program, eligibility, curriculum, "
            "practical learning, industry training, and career opportunities.\n\n"
            "Please choose an option below 👇"
        )
    )

    footer = MessageFooter(
        text="🎓 GM University Admissions 2026-27"
    )

    btn_program_details = Button(reply=ButtonReply(id="bdaba", title="Program Details"))
    btn_fee_duration = Button(reply=ButtonReply(id="bdabb", title="Fee Details"))
    btn_branch_website = Button(reply=ButtonReply(id="bdabc", title="More Info"))

    action = ButtonAction(buttons=[btn_program_details, btn_fee_duration, btn_branch_website])

    interactive = InteractiveButton(
        header=header,
        body=body,
        footer=footer,
        action=action,
    )

    payload = WhatsAppInteractiveButtonRequest(to=wa_id, interactive=interactive)
    return payload.model_dump()


def build_mcom_fae_program_details_payload(wa_id: str):
    """Builds a WhatsApp text payload for M.Com Fintech Analytics and Entrepreneurship program details."""

    text = (
        "🎓 *M.Com in Fintech Analytics and Entrepreneurship*\n"
        "📘 *Program Details – 2026-27 Intake*\n\n"

        "━━━━━━━━━━━━━━━\n"
        "📄 *Program Document Includes:*\n"
        "• Curriculum Structure\n"
        "• Eligibility Criteria\n"
        "• Fintech and Analytics Core Subjects\n"
        "• Entrepreneurship and Startup Concepts\n"
        "• Digital Finance and Business Learning\n"
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


def build_mcom_fae_fee_duration_payload(wa_id: str):
    """Builds a WhatsApp text payload for M.Com Fintech Analytics and Entrepreneurship fee information."""

    text = (
        "🎓 *GM University – M.Com Fintech Analytics and Entrepreneurship Fee Details*\n\n"

        "⏱ *Duration:* 2 Years\n"
        "💰 *Program Annual Fee:* ₹52,500\n\n"

        "📘 *Program Information:*\n"
        "━━━━━━━━━━━━━━━\n"
        "• Fintech analytics and entrepreneurship focused postgraduate program\n"
        "• Strong foundation in digital finance, analytics and financial markets\n"
        "• Startup, innovation and entrepreneurship-based learning\n"
        "• Industry-oriented practical training\n"
        "• Career opportunities in fintech, banking, finance, startups, analytics and business sectors\n"
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


def build_mcom_fae_branch_website_payload(wa_id: str):
    """Builds a WhatsApp text payload for M.Com Fintech Analytics and Entrepreneurship information."""

    text = (
        "💳📈 *GM University – M.Com Fintech Analytics and Entrepreneurship*\n\n"

        "🔗 *Official Program Document:*\n"
        "https://gmu.ac.in/pdfview_assets%5Cdownloadmaterial%5Cschoolofcommerce%5CMCom%20Program%20Document%202025-26.pdf"

        "Stay connected with GM University for updates regarding:\n"
        "━━━━━━━━━━━━━━━\n"
        "• Program Overview\n"
        "• Curriculum Details\n"
        "• Fintech Analytics Training\n"
        "• Entrepreneurship Learning\n"
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
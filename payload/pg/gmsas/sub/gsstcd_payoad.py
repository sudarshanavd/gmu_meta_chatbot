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


def build_mtech_stcd_program_payload(wa_id: str):
    """Builds the payload for the M.Tech Semiconductor Technologies and Chip Design program."""

    header = MessageHeader(
        text="🔬💻 M.Tech Semiconductor Technologies and Chip Design"
    )

    body = MessageBody(
        text=(
            "🎓 *M.Tech in Semiconductor Technologies and Chip Design*\n\n"
            "Learn core concepts in:\n"
            "• Semiconductor Devices\n"
            "• VLSI Design\n"
            "• Digital IC Design\n"
            "• Analog IC Design\n"
            "• Chip Design Flow\n"
            "• CMOS Technology\n"
            "• Embedded Systems\n"
            "• Electronic Design Automation\n"
            "• FPGA and ASIC Design\n"
            "• Semiconductor Manufacturing Concepts\n\n"
            "Get details about the program, eligibility, curriculum, "
            "training, practical learning, and career opportunities.\n\n"
            "Please choose an option below 👇"
        )
    )

    footer = MessageFooter(
        text="🎓 GM University Admissions 2026-27"
    )

    btn_program_details = Button(reply=ButtonReply(id="baaka", title="Program Details"))
    btn_fee_duration = Button(reply=ButtonReply(id="baakb", title="Fee Details"))
    btn_branch_website = Button(reply=ButtonReply(id="baakc", title="More Info"))

    action = ButtonAction(buttons=[btn_program_details, btn_fee_duration, btn_branch_website])

    interactive = InteractiveButton(
        header=header,
        body=body,
        footer=footer,
        action=action,
    )

    payload = WhatsAppInteractiveButtonRequest(to=wa_id, interactive=interactive)
    return payload.model_dump()


def build_mtech_stcd_program_details_payload(wa_id: str):
    """Builds a WhatsApp text payload for M.Tech Semiconductor Technologies and Chip Design program details."""

    text = (
        "🎓 *M.Tech in Semiconductor Technologies and Chip Design*\n"
        "📘 *Program Details – 2026-27 Intake*\n\n"

        "━━━━━━━━━━━━━━━\n"
        "📄 *Program Document Includes:*\n"
        "• Curriculum Structure\n"
        "• Eligibility Criteria\n"
        "• Semiconductor Technology Core Subjects\n"
        "• Chip Design and VLSI Concepts\n"
        "• Digital, Analog and Embedded System Learning\n"
        "• Practical & Industry-Oriented Training\n"
        "• Research and Career Opportunities\n"
        "━━━━━━━━━━━━━━━\n\n"

        "🔗 *View Full Program Document:*\n"
        "https://gmu.ac.in/pdfview_assets%5Cdownloadmaterial%5CGMU%20School%20of%20Advanced%20%20Studies%20%20Pdf%20Final%5CECE%20M.Tech%20-%20Program%20Document.pdf"

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


def build_mtech_stcd_fee_duration_payload(wa_id: str):
    """Builds a WhatsApp text payload for M.Tech Semiconductor Technologies and Chip Design fee information."""

    text = (
        "🎓 *GM University – M.Tech Semiconductor Technologies and Chip Design Fee Details*\n\n"

        "📌 Fee details\n"
        "━━━━━━━━━━━━━━━\n"
        "₹1,25,000\n\n"

        "⏳ *Program Duration*\n"
        "━━━━━━━━━━━━━━━\n"
        "2 Years \n\n"

        "📘 *Program Information:*\n"
        "━━━━━━━━━━━━━━━\n"
        "• Semiconductor technology and chip design focused program\n"
        "• VLSI, IC design and CMOS technology based learning\n"
        "• Digital, analog, FPGA and ASIC design concepts\n"
        "• Industry-oriented practical training\n"
        "• Career opportunities in semiconductor, VLSI, embedded systems and chip design sectors\n"
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


def build_mtech_stcd_branch_website_payload(wa_id: str):
    """Builds a WhatsApp text payload for M.Tech Semiconductor Technologies and Chip Design information."""

    text = (
        "🔬💻 *GM University – M.Tech Semiconductor Technologies and Chip Design*\n\n"

        "🔗 *Official Program Document:*\n"
        "https://gmu.ac.in/pdfview_assets%5Cdownloadmaterial%5CGMU%20School%20of%20Advanced%20%20Studies%20%20Pdf%20Final%5CECE%20M.Tech%20-%20Program%20Document.pdf"
        "Stay connected with GM University for updates regarding:\n"
        "━━━━━━━━━━━━━━━\n"
        "• Program Overview\n"
        "• Curriculum Details\n"
        "• Practical Training\n"
        "• Semiconductor Technology Projects\n"
        "• Chip Design and VLSI Learning\n"
        "• Admission Information\n"
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
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


def build_msc_cyber_security_program_payload(wa_id: str):
    """Builds the payload for the M.Sc Cyber Security program."""

    header = MessageHeader(
        text="🛡️💻 M.Sc Cyber Security"
    )

    body = MessageBody(
        text=(
            "Learn core concepts in:\n"
            "• Python Programming\n"
            "• Data Structures and Algorithms\n"
            "• Database Management Systems\n"
            "• Cyber Security Fundamentals\n"
            "• Network Security\n"
            "• Ethical Hacking\n"
            "• Cryptography\n"
            "• Digital Forensics\n"
            "• Web Application Security\n"
            "• Cloud Security\n\n"
            "Get details about the program, eligibility, curriculum, "
            "practical learning, research training, and career opportunities.\n\n"
            "Please choose an option below 👇"
        )
    )

    footer = MessageFooter(
        text="🎓 GM University Admissions 2026-27"
    )

    btn_program_details = Button(reply=ButtonReply(id="bbcga", title="Program Details"))
    btn_fee_duration = Button(reply=ButtonReply(id="bbcfb", title="Fee Details"))
    btn_branch_website = Button(reply=ButtonReply(id="bbcfc", title="More Info"))

    action = ButtonAction(buttons=[btn_program_details, btn_fee_duration, btn_branch_website])

    interactive = InteractiveButton(
        header=header,
        body=body,
        footer=footer,
        action=action,
    )

    payload = WhatsAppInteractiveButtonRequest(to=wa_id, interactive=interactive)
    return payload.model_dump()


def build_msc_cyber_security_program_details_payload(wa_id: str):
    """Builds a WhatsApp text payload for M.Sc Cyber Security program details."""

    text = (
        "🎓 *M.Sc in Cyber Security*\n"
        "📘 *Program Details – 2026-27 Intake*\n\n"

        "━━━━━━━━━━━━━━━\n"
        "📄 *Program Document Includes:*\n"
        "• Curriculum Structure\n"
        "• Eligibility Criteria\n"
        "• Cyber Security Core Subjects\n"
        "• Network Security and Ethical Hacking Concepts\n"
        "• Cryptography and Digital Forensics Learning\n"
        "• Practical & Project-Based Training\n"
        "• Career Opportunities\n"
        "━━━━━━━━━━━━━━━\n\n"

        "🔗 *View Full Program Document:*\n"
        "https://gmu.ac.in/pdfview_assets%5Cdownloadmaterial%5CSchool%20of%20Computer%20Science%20-Program%20Docs%5CM.Sc-Cyber%20Security%20%282025-26%20Scheme%29.pdf"

        "\n\n📞 *Contact Details*\n"
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


def build_msc_cyber_security_fee_duration_payload(wa_id: str):
    """Builds a WhatsApp text payload for M.Sc Cyber Security fee information."""

    text = (
        "🎓 *GM University – M.Sc Cyber Security Fee Details*\n\n"

        "⏱ *Duration:* 2 Years\n"
        "💰 *Program Annual Fee:* ₹1,12,500\n\n"

        "📘 *Program Information:*\n"
        "━━━━━━━━━━━━━━━\n"
        "• Advanced cyber security focused postgraduate program\n"
        "• Strong foundation in networks, ethical hacking and secure systems\n"
        "• Practical and project-based learning\n"
        "• Research and industry-oriented training\n"
        "• Career opportunities in cybersecurity, ethical hacking, digital forensics, cloud security and IT services\n"
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


def build_msc_cyber_security_branch_website_payload(wa_id: str):
    """Builds a WhatsApp text payload for M.Sc Cyber Security information."""

    text = (
        "🛡️💻 *GM University – M.Sc Cyber Security*\n\n"

        "🔗 *Official Program Document:*\n"
        "https://gmu.ac.in/pdfview_assets%5Cdownloadmaterial%5CSchool%20of%20Computer%20Science%20-Program%20Docs%5CM.Sc-Cyber%20Security%20%282025-26%20Scheme%29.pdf"
        "Stay connected with GM University for updates regarding:\n"
        "━━━━━━━━━━━━━━━\n"
        "• Program Overview\n"
        "• Curriculum Details\n"
        "• Cyber Security Training\n"
        "• Ethical Hacking Projects\n"
        "• Digital Forensics Learning\n"
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
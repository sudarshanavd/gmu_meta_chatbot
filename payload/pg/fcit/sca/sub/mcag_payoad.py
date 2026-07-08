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

def build_mca_program_payload(wa_id: str):
    """Builds the payload for the MCA program."""

    header = MessageHeader(
        text="💻🚀 Master of Computer Applications (MCA)"
    )

    body = MessageBody(
        text=(
            "Learn core concepts in:\n"
            "• Programming Languages\n"
            "• Data Structures and Algorithms\n"
            "• Database Management Systems\n"
            "• Software Engineering\n"
            "• Computer Networks\n"
            "• Web Technologies\n"
            "• Cloud Computing\n"
            "• Artificial Intelligence\n"
            "• Cyber Security\n"
            "• Mobile Application Development\n\n"
            "Get details about the program, eligibility, curriculum, "
            "practical learning, industry training, and career opportunities.\n\n"
            "Please choose an option below 👇"
        )
    )

    footer = MessageFooter(
        text="🎓 GM University Admissions 2026-27"
    )

    btn_program_details = Button(reply=ButtonReply(id="bbcaa", title="Program Details"))
    btn_fee_duration = Button(reply=ButtonReply(id="bbcab", title="Fee Details"))
    btn_branch_website = Button(reply=ButtonReply(id="bbcac", title="More Info"))

    action = ButtonAction(buttons=[btn_program_details, btn_fee_duration, btn_branch_website])

    interactive = InteractiveButton(
        header=header,
        body=body,
        footer=footer,
        action=action,
    )

    payload = WhatsAppInteractiveButtonRequest(to=wa_id, interactive=interactive)
    return payload.model_dump()


def build_mca_program_details_payload(wa_id: str):
    """Builds a WhatsApp text payload for MCA program details."""

    text = (
        "🎓 *Master of Computer Applications (MCA)*\n"
        "📘 *Program Details – 2026-27 Intake*\n\n"

        "━━━━━━━━━━━━━━━\n"
        "📄 *Program Document Includes:*\n"
        "• Curriculum Structure\n"
        "• Eligibility Criteria\n"
        "• Computer Application Core Subjects\n"
        "• Software Development Concepts\n"
        "• Industry-Oriented Learning\n"
        "• Practical & Project-Based Training\n"
        "• Career Opportunities\n"
        "━━━━━━━━━━━━━━━\n\n"

        "🔗 *View Full Program Document:*\n"
        "https://gmu.ac.in/pdfview_assets%5Cdownloadmaterial%5CSchool%20of%20Computer%20Applications-Program%20Docs%5CMCA%20Program%20Document%202025.pdf"
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


def build_mca_fee_duration_payload(wa_id: str):
    """Builds a WhatsApp text payload for MCA fee information."""

    text = (
        "🎓 *GM University – MCA Fee Details*\n\n"

        "⏱ *Duration:* 2 Years\n"
        "💰 *Program Annual Fee:* ₹1,35,000\n\n"

        "📘 *Program Information:*\n"
        "━━━━━━━━━━━━━━━\n"
        "• Industry-focused postgraduate computer applications program\n"
        "• Strong foundation in software development and emerging technologies\n"
        "• Practical and project-based learning\n"
        "• Industry-oriented training and internships\n"
        "• Career opportunities in software development, cloud computing, AI, cybersecurity and IT services\n"
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


def build_mca_branch_website_payload(wa_id: str):
    """Builds a WhatsApp text payload for MCA information."""

    text = (
        "💻🚀 *GM University – Master of Computer Applications (MCA)*\n\n"

        "🔗 *Official Program Document:*\n"
        "https://gmu.ac.in/pdfview_assets%5Cdownloadmaterial%5CSchool%20of%20Computer%20Applications-Program%20Docs%5CMCA%20Program%20Document%202025.pdf\n\n"

        "Stay connected with GM University for updates regarding:\n"
        "━━━━━━━━━━━━━━━\n"
        "• Program Overview\n"
        "• Curriculum Details\n"
        "• Software Development Training\n"
        "• Industry Projects\n"
        "• Placement Opportunities\n"
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
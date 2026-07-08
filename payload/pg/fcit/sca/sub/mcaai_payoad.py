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

def build_mca_ai_data_analytics_program_payload(wa_id: str):
    """Builds the payload for the MCA AI and Data Analytics program."""

    header = MessageHeader(
        text="🤖📊 MCA AI and Data Analytics"
    )

    body = MessageBody(
        text=(
            "Learn core concepts in:\n"
            "• Programming Languages\n"
            "• Data Structures and Algorithms\n"
            "• Database Management Systems\n"
            "• Artificial Intelligence\n"
            "• Machine Learning\n"
            "• Data Analytics\n"
            "• Python for Data Science\n"
            "• Big Data Technologies\n"
            "• Data Visualization\n"
            "• Cloud Computing\n\n"
            "Get details about the program, eligibility, curriculum, "
            "practical learning, industry training, and career opportunities.\n\n"
            "Please choose an option below 👇"
        )
    )

    footer = MessageFooter(
        text="🎓 GM University Admissions 2026-27"
    )

    btn_program_details = Button(reply=ButtonReply(id="bbcda", title="Program Details"))
    btn_fee_duration = Button(reply=ButtonReply(id="bbcdb", title="Fee Details"))
    btn_branch_website = Button(reply=ButtonReply(id="bbcdc", title="More Info"))

    action = ButtonAction(buttons=[btn_program_details, btn_fee_duration, btn_branch_website])

    interactive = InteractiveButton(
        header=header,
        body=body,
        footer=footer,
        action=action,
    )

    payload = WhatsAppInteractiveButtonRequest(to=wa_id, interactive=interactive)
    return payload.model_dump()


def build_mca_ai_data_analytics_program_details_payload(wa_id: str):
    """Builds a WhatsApp text payload for MCA AI and Data Analytics program details."""

    text = (
        "🎓 *MCA in AI and Data Analytics*\n"
        "📘 *Program Details – 2026-27 Intake*\n\n"

        "━━━━━━━━━━━━━━━\n"
        "📄 *Program Document Includes:*\n"
        "• Curriculum Structure\n"
        "• Eligibility Criteria\n"
        "• Computer Application Core Subjects\n"
        "• Artificial Intelligence and Machine Learning Concepts\n"
        "• Data Analytics and Visualization Learning\n"
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


def build_mca_ai_data_analytics_fee_duration_payload(wa_id: str):
    """Builds a WhatsApp text payload for MCA AI and Data Analytics fee information."""

    text = (
        "🎓 *GM University – MCA AI and Data Analytics Fee Details*\n\n"

        "⏱ *Duration:* 2 Years\n"
        "💰 *Program Annual Fee:* ₹1,35,000\n\n"

        "📘 *Program Information:*\n"
        "━━━━━━━━━━━━━━━\n"
        "• Industry-focused postgraduate computer applications program\n"
        "• Strong foundation in AI, machine learning and data analytics\n"
        "• Practical and project-based learning\n"
        "• Industry-oriented training and internships\n"
        "• Career opportunities in AI, data analytics, machine learning, cloud computing and IT services\n"
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


def build_mca_ai_data_analytics_branch_website_payload(wa_id: str):
    """Builds a WhatsApp text payload for MCA AI and Data Analytics information."""

    text = (
        "🤖📊 *GM University – MCA AI and Data Analytics*\n\n"

        "🔗 *Official Program Document:*\n"
        "https://gmu.ac.in/pdfview_assets%5Cdownloadmaterial%5CSchool%20of%20Computer%20Applications-Program%20Docs%5CMCA%20Program%20Document%202025.pdf"
        "Stay connected with GM University for updates regarding:\n"
        "━━━━━━━━━━━━━━━\n"
        "• Program Overview\n"
        "• Curriculum Details\n"
        "• AI and Data Analytics Training\n"
        "• Machine Learning Projects\n"
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
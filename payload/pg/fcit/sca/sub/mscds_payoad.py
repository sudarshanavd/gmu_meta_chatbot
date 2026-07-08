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


def build_msc_data_science_program_payload(wa_id: str):
    """Builds the payload for the M.Sc Data Science program."""

    header = MessageHeader(
        text="🎓M.Sc Data Science"
    )

    body = MessageBody(
        text=(
            "Learn core concepts in:\n"
            "• Python Programming\n"
            "• Data Structures and Algorithms\n"
            "• Database Management Systems\n"
            "• Data Science Fundamentals\n"
            "• Statistics for Data Science\n"
            "• Machine Learning\n"
            "• Artificial Intelligence\n"
            "• Big Data Analytics\n"
            "• Data Visualization\n"
            "• Cloud Computing\n\n"
            "Get details about the program, eligibility, curriculum, "
            "practical learning, research training, and career opportunities.\n\n"
            "Please choose an option below 👇"
        )
    )

    footer = MessageFooter(
        text="🎓 GM University Admissions 2026-27"
    )

    btn_program_details = Button(reply=ButtonReply(id="bbcea", title="Program Details"))
    btn_fee_duration = Button(reply=ButtonReply(id="bbceb", title="Fee Details"))
    btn_branch_website = Button(reply=ButtonReply(id="bbcec", title="More Info"))

    action = ButtonAction(buttons=[btn_program_details, btn_fee_duration, btn_branch_website])

    interactive = InteractiveButton(
        header=header,
        body=body,
        footer=footer,
        action=action,
    )

    payload = WhatsAppInteractiveButtonRequest(to=wa_id, interactive=interactive)
    return payload.model_dump()


def build_msc_data_science_program_details_payload(wa_id: str):
    """Builds a WhatsApp text payload for M.Sc Data Science program details."""

    text = (
        "🎓 *M.Sc in Data Science*\n"
        "📘 *Program Details – 2026-27 Intake*\n\n"

        "━━━━━━━━━━━━━━━\n"
        "📄 *Program Document Includes:*\n"
        "• Curriculum Structure\n"
        "• Eligibility Criteria\n"
        "• Data Science Core Subjects\n"
        "• Statistics, AI and Machine Learning Concepts\n"
        "• Big Data and Data Visualization Learning\n"
        "• Practical & Project-Based Training\n"
        "• Career Opportunities\n"
        "━━━━━━━━━━━━━━━\n\n"

        "🔗 *View Full Program Document:*\n"
        "https://gmu.ac.in/pdfview_assets%5Cdownloadmaterial%5CSchool%20of%20Computer%20Science%20-Program%20Docs%5CM.Sc-DS%20%282025-26%20Scheme%29.pdf"
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


def build_msc_data_science_fee_duration_payload(wa_id: str):
    """Builds a WhatsApp text payload for M.Sc Data Science fee information."""

    text = (
        "🎓 *GM University – M.Sc Data Science Fee Details*\n\n"

        "⏱ *Duration:* 2 Years\n"
        "💰 *Program Annual Fee:* ₹1,12,500\n\n"

        "📘 *Program Information:*\n"
        "━━━━━━━━━━━━━━━\n"
        "• Advanced data science focused postgraduate program\n"
        "• Strong foundation in statistics, AI, machine learning and analytics\n"
        "• Practical and project-based learning\n"
        "• Research and industry-oriented training\n"
        "• Career opportunities in data science, AI, analytics, big data, cloud computing and IT services\n"
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


def build_msc_data_science_branch_website_payload(wa_id: str):
    """Builds a WhatsApp text payload for M.Sc Data Science information."""

    text = (
        "📊🤖 *GM University – M.Sc Data Science*\n\n"

        "🔗 *Official Program Document:*\n"
        "https://gmu.ac.in/pdfview_assets%5Cdownloadmaterial%5CSchool%20of%20Computer%20Science%20-Program%20Docs%5CM.Sc-DS%20%282025-26%20Scheme%29.pdf\n\n"

        "Stay connected with GM University for updates regarding:\n"
        "━━━━━━━━━━━━━━━\n"
        "• Program Overview\n"
        "• Curriculum Details\n"
        "• Data Science Training\n"
        "• Machine Learning Projects\n"
        "• Big Data and Analytics Learning\n"
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
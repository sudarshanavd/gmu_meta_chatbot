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


def build_msc_ai_data_analytics_program_payload(wa_id: str):
    """Builds the payload for the M.Sc AI and Data Analytics program."""

    header = MessageHeader(
        text="🤖📊 M.Sc AI and Data Analytics"
    )

    body = MessageBody(
        text=(
            
            "Learn core concepts in:\n"
            "• Python Programming\n"
            "• Data Structures and Algorithms\n"
            "• Database Management Systems\n"
            "• Artificial Intelligence\n"
            "• Machine Learning\n"
            "• Deep Learning\n"
            "• Data Analytics\n"
            "• Big Data Technologies\n"
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

    btn_program_details = Button(reply=ButtonReply(id="bbcfa", title="Program Details"))
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


def build_msc_ai_data_analytics_program_details_payload(wa_id: str):
    """Builds a WhatsApp text payload for M.Sc AI and Data Analytics program details."""

    text = (
        "🎓 *M.Sc in AI and Data Analytics*\n"
        "📘 *Program Details – 2026-27 Intake*\n\n"

        "━━━━━━━━━━━━━━━\n"
        "📄 *Program Document Includes:*\n"
        "• Curriculum Structure\n"
        "• Eligibility Criteria\n"
        "• AI and Data Analytics Core Subjects\n"
        "• Machine Learning and Deep Learning Concepts\n"
        "• Big Data and Data Visualization Learning\n"
        "• Practical & Project-Based Training\n"
        "• Career Opportunities\n"
        "━━━━━━━━━━━━━━━\n\n"

        "🔗 *View Full Program Document:*\n"
        "https://gmu.ac.in/pdfview_assets%5Cdownloadmaterial%5CSchool%20of%20Computer%20Science%20-Program%20Docs%5CM.Sc-AI%20&%20DA%20%282025-26%20Scheme%29.pdf"

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


def build_msc_ai_data_analytics_fee_duration_payload(wa_id: str):
    """Builds a WhatsApp text payload for M.Sc AI and Data Analytics fee information."""

    text = (
        "🎓 *GM University – M.Sc AI and Data Analytics Fee Details*\n\n"

        "⏱ *Duration:* 2 Years\n"
        "💰 *Program Annual Fee:* ₹1,12,500\n\n"

        "📘 *Program Information:*\n"
        "━━━━━━━━━━━━━━━\n"
        "• Advanced AI and data analytics focused postgraduate program\n"
        "• Strong foundation in machine learning, deep learning and analytics\n"
        "• Practical and project-based learning\n"
        "• Research and industry-oriented training\n"
        "• Career opportunities in AI, data analytics, machine learning, big data, cloud computing and IT services\n"
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


def build_msc_ai_data_analytics_branch_website_payload(wa_id: str):
    """Builds a WhatsApp text payload for M.Sc AI and Data Analytics information."""

    text = (
        "🤖📊 *GM University – M.Sc AI and Data Analytics*\n\n"

        "🔗 *Official Program Document:*\n"
        "https://gmu.ac.in/pdfview_assets%5Cdownloadmaterial%5CSchool%20of%20Computer%20Science%20-Program%20Docs%5CM.Sc-AI%20&%20DA%20%282025-26%20Scheme%29.pdf"
        "Stay connected with GM University for updates regarding:\n"
        "━━━━━━━━━━━━━━━\n"
        "• Program Overview\n"
        "• Curriculum Details\n"
        "• AI and Data Analytics Training\n"
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
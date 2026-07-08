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

def build_mtech_de_program_payload(wa_id: str):
    """Builds the payload for the M.Tech Data Engineering program."""

    header = MessageHeader(
        text="📊⚙️ M.Tech Data Engineering"
    )

    body = MessageBody(
        text=(
            "🎓 *M.Tech in Data Engineering*\n\n"
            "Learn core concepts in:\n"
            "• Data Engineering Fundamentals\n"
            "• Big Data Technologies\n"
            "• Data Warehousing\n"
            "• Data Pipelines and ETL\n"
            "• Database Management Systems\n"
            "• Cloud Data Platforms\n"
            "• Distributed Computing\n"
            "• Data Modeling\n"
            "• Data Analytics\n"
            "• Machine Learning Operations\n\n"
            "Get details about the program, eligibility, curriculum, "
            "training, practical learning, and career opportunities.\n\n"
            "Please choose an option below 👇"
        )
    )

    footer = MessageFooter(
        text="🎓 GM University Admissions 2026-27"
    )

    btn_program_details = Button(reply=ButtonReply(id="baaca", title="Program Details"))
    btn_fee_duration = Button(reply=ButtonReply(id="baacb", title="Fee Details"))
    btn_branch_website = Button(reply=ButtonReply(id="baacc", title="More Info"))

    action = ButtonAction(buttons=[btn_program_details, btn_fee_duration, btn_branch_website])

    interactive = InteractiveButton(
        header=header,
        body=body,
        footer=footer,
        action=action,
    )

    payload = WhatsAppInteractiveButtonRequest(to=wa_id, interactive=interactive)
    return payload.model_dump()


def build_mtech_de_program_details_payload(wa_id: str):
    """Builds a well-formatted WhatsApp text payload for full M.Tech Data Engineering program details."""

    text = (
        "🎓 *M.Tech in Data Engineering*\n"
        "📘 *Program Details – 2026-27 Intake*\n\n"

        "━━━━━━━━━━━━━━━\n"
        "📄 *Program Document Includes:*\n"
        "• Curriculum Structure\n"
        "• Eligibility Criteria\n"
        "• Data Engineering Core Subjects\n"
        "• Big Data & Cloud Data Concepts\n"
        "• Practical & Industry-Oriented Learning\n"
        "• Academic & Career Opportunities\n"
        "━━━━━━━━━━━━━━━\n\n"

        "🔗 *View Full Program Document:*\n"
        "https://gmu.ac.in/imgview?dummy=data2024&base=assets%2Fdownloadmaterial%2FGMU%20School%20of%20Advanced%20%20Studies%20%20Pdf%20Final%2FData%20Engineering%2FData%20Engineering-&ext=png"

        "\n\n📞 *Contact Details*\n"
        "━━━━━━━━━━━━━━━\n"
        "📍 GM University, Davangere\n"
        "☎️ Phone: +91 9364099712,+91 9364099720\n"
        # "📧 Email: mtech.dataengineering@gmu.ac.in\n"
    )

    payload = WhatsAppTextReplyRequest(
        to=wa_id,
        text=TextBody(
            body=text,
            preview_url=True
        ),
    )

    return payload.model_dump()


def build_mtech_de_fee_duration_payload(wa_id: str):
    """Builds a well-formatted WhatsApp text payload for M.Tech Data Engineering fee information."""

    text = (
        "🎓 *GM University – M.Tech Data Engineering Fee Details*\n\n"

        "📌 Fee details\n"
        "━━━━━━━━━━━━━━━\n"
        "₹1,25,000\n\n"

        "⏳ *Program Duration*\n"
        "━━━━━━━━━━━━━━━\n"
        "2 Years \n\n"

        "📘 *Program Information:*\n"
        "━━━━━━━━━━━━━━━\n"
        "• Advanced data engineering focused program\n"
        "• Big data and cloud data platform learning\n"
        "• Data pipeline and ETL practical training\n"
        "• Industry-oriented data infrastructure concepts\n"
        "• Career opportunities in data engineering, analytics and cloud sectors\n"
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


def build_mtech_de_branch_website_payload(wa_id: str):
    """Builds a well-formatted WhatsApp text payload for M.Tech Data Engineering information."""

    text = (
        "📊⚙️ *GM University – M.Tech Data Engineering*\n\n"

        "📌 Official website/link will be updated soon.\n\n"

        "Stay connected with GM University for updates regarding:\n"
        "━━━━━━━━━━━━━━━\n"
        "• Program Overview\n"
        "• Curriculum Details\n"
        "• Practical Training\n"
        "• Data Engineering Lab Learning\n"
        "• Big Data Projects\n"
        "• Admission Information\n"
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
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


def build_mtech_isiiot_program_payload(wa_id: str):
    """Builds the payload for the M.Tech Intelligent Systems and Industrial IoT program."""

    header = MessageHeader(
        text="🤖🏭 M.Tech Intelligent Systems and Industrial IoT"
    )

    body = MessageBody(
        text=(
            "🎓 *M.Tech in Intelligent Systems and Industrial IoT*\n\n"
            "Learn core concepts in:\n"
            "• Artificial Intelligence\n"
            "• Machine Learning\n"
            "• Industrial Internet of Things\n"
            "• Smart Sensors and Actuators\n"
            "• Embedded Systems\n"
            "• Automation and Control Systems\n"
            "• Data Analytics for Industry\n"
            "• Cyber-Physical Systems\n"
            "• Robotics and Intelligent Machines\n"
            "• Industry 4.0 Technologies\n\n"
            "Get details about the program, eligibility, curriculum, "
            "training, practical learning, and career opportunities.\n\n"
            "Please choose an option below 👇"
        )
    )

    footer = MessageFooter(
        text="🎓 GM University Admissions 2026-27"
    )

    btn_program_details = Button(reply=ButtonReply(id="baaja", title="Program Details"))
    btn_fee_duration = Button(reply=ButtonReply(id="baajb", title="Fee Details"))
    btn_branch_website = Button(reply=ButtonReply(id="baajc", title="More Info"))

    action = ButtonAction(buttons=[btn_program_details, btn_fee_duration, btn_branch_website])

    interactive = InteractiveButton(
        header=header,
        body=body,
        footer=footer,
        action=action,
    )

    payload = WhatsAppInteractiveButtonRequest(to=wa_id, interactive=interactive)
    return payload.model_dump()


def build_mtech_isiiot_program_details_payload(wa_id: str):
    """Builds a WhatsApp text payload for M.Tech Intelligent Systems and Industrial IoT program details."""

    text = (
        "🎓 *M.Tech in Intelligent Systems and Industrial IoT*\n"
        "📘 *Program Details – 2026-27 Intake*\n\n"

        "━━━━━━━━━━━━━━━\n"
        "📄 *Program Document Includes:*\n"
        "• Curriculum Structure\n"
        "• Eligibility Criteria\n"
        "• Intelligent Systems Core Subjects\n"
        "• Industrial IoT and Automation Concepts\n"
        "• AI, ML and Data Analytics Learning\n"
        "• Practical & Industry-Oriented Training\n"
        "• Research and Career Opportunities\n"
        "━━━━━━━━━━━━━━━\n\n"

        "🔗 *View Full Program Document:*\n"
        "https://gmu.ac.in/pdfview_assets%5Cdownloadmaterial%5CGMU%20School%20of%20Advanced%20%20Studies%20%20Pdf%20Final%5C2.%20AI&IoT-PgD_PD.pdf"

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


def build_mtech_isiiot_fee_duration_payload(wa_id: str):
    """Builds a WhatsApp text payload for M.Tech Intelligent Systems and Industrial IoT fee information."""

    text = (
        "🎓 *GM University – M.Tech Intelligent Systems and Industrial IoT Fee Details*\n\n"

        "📌 Fee details\n"
        "━━━━━━━━━━━━━━━\n"
        "₹1,25,000\n\n"

        "⏳ *Program Duration*\n"
        "━━━━━━━━━━━━━━━\n"
        "2 Years \n\n"

        "📘 *Program Information:*\n"
        "━━━━━━━━━━━━━━━\n"
        "• Intelligent systems and industrial automation focused program\n"
        "• AI, ML and Industrial IoT based learning\n"
        "• Smart sensors, embedded systems and cyber-physical system concepts\n"
        "• Industry-oriented practical training\n"
        "• Career opportunities in Industry 4.0, automation, robotics, IoT and intelligent systems\n"
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


def build_mtech_isiiot_branch_website_payload(wa_id: str):
    """Builds a WhatsApp text payload for M.Tech Intelligent Systems and Industrial IoT information."""

    text = (
        "🤖🏭 *GM University – M.Tech Intelligent Systems and Industrial IoT*\n\n"

        "🔗 *Official Program Document:*\n"
        "https://gmu.ac.in/pdfview_assets%5Cdownloadmaterial%5CGMU%20School%20of%20Advanced%20%20Studies%20%20Pdf%20Final%5C2.%20AI&IoT-PgD_PD.pdf"
        "Stay connected with GM University for updates regarding:\n"
        "━━━━━━━━━━━━━━━\n"
        "• Program Overview\n"
        "• Curriculum Details\n"
        "• Practical Training\n"
        "• Intelligent Systems Projects\n"
        "• Industrial IoT and Automation Learning\n"
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
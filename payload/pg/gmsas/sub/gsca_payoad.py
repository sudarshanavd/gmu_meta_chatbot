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

def build_mtech_case_program_payload(wa_id: str):
    """Builds the payload for the M.Tech Computer Aided Structural Engineering program."""

    header = MessageHeader(
        text="🏗️💻 M.Tech CASE"
    )

    body = MessageBody(
        text=(
            "🎓 *M.Tech in Computer Aided Structural Engineering (CASE)*\n\n"
            "Learn core concepts in:\n"
            "• Structural Analysis\n"
            "• Advanced Concrete Design\n"
            "• Steel Structure Design\n"
            "• Finite Element Analysis\n"
            "• Computer Aided Design\n"
            "• Structural Dynamics\n"
            "• Earthquake Resistant Design\n"
            "• Bridge Engineering\n"
            "• Construction Materials\n"
            "• Structural Modeling and Simulation\n\n"
            "Get details about the program, eligibility, curriculum, "
            "training, practical learning, and career opportunities.\n\n"
            "Please choose an option below 👇"
        )
    )

    footer = MessageFooter(
        text="🎓 GM University Admissions 2026-27"
    )

    btn_program_details = Button(reply=ButtonReply(id="baada", title="Program Details"))
    btn_fee_duration = Button(reply=ButtonReply(id="baadb", title="Fee Details"))
    btn_branch_website = Button(reply=ButtonReply(id="baadc", title="More Info"))

    action = ButtonAction(buttons=[btn_program_details, btn_fee_duration, btn_branch_website])

    interactive = InteractiveButton(
        header=header,
        body=body,
        footer=footer,
        action=action,
    )

    payload = WhatsAppInteractiveButtonRequest(to=wa_id, interactive=interactive)
    return payload.model_dump()


def build_mtech_case_program_details_payload(wa_id: str):
    """Builds a well-formatted WhatsApp text payload for full M.Tech CASE program details."""

    text = (
        "🎓 *M.Tech in Computer Aided Structural Engineering (CASE)*\n"
        "📘 *Program Details – 2026-27 Intake*\n\n"

        "━━━━━━━━━━━━━━━\n"
        "📄 *Program Document Includes:*\n"
        "• Curriculum Structure\n"
        "• Eligibility Criteria\n"
        "• CASE Core Subjects\n"
        "• Structural Design & Analysis Concepts\n"
        "• Practical & Industry-Oriented Learning\n"
        "• Academic & Career Opportunities\n"
        "━━━━━━━━━━━━━━━\n\n"

        "🔗 *View Full Program Document:*\n"
        "https://gmu.ac.in/imgview?dummy=data2024&base=assets%2Fdownloadmaterial%2FGMU%20School%20of%20Advanced%20%20Studies%20%20Pdf%20Final%2FComputer%20Aided%20Structural%2FComputer%20Aided%20Structural-&ext=png"
        "\n\n📞 *Contact Details*\n"
        "━━━━━━━━━━━━━━━\n"
        "📍 GM University, Davangere\n"
        "☎️ Phone: +91 9364099712,+91 9364099720\n"
        # "📧 Email: mtech.case@gmu.ac.in\n"
    )

    payload = WhatsAppTextReplyRequest(
        to=wa_id,
        text=TextBody(
            body=text,
            preview_url=True
        ),
    )

    return payload.model_dump()


def build_mtech_case_fee_duration_payload(wa_id: str):
    """Builds a well-formatted WhatsApp text payload for M.Tech CASE fee information."""

    text = (
        "🎓 *GM University – M.Tech CASE Fee Details*\n\n"

        "📌 Fee details\n"
        "━━━━━━━━━━━━━━━\n"
        "₹1,25,000\n\n"

        "⏳ *Program Duration*\n"
        "━━━━━━━━━━━━━━━\n"
        "2 Years \n\n"

        "📘 *Program Information:*\n"
        "━━━━━━━━━━━━━━━\n"
        "• Advanced structural engineering focused program\n"
        "• Computer aided structural analysis and design\n"
        "• CAD and simulation-based practical training\n"
        "• Industry-oriented structural modeling concepts\n"
        "• Career opportunities in structural design, construction and consultancy sectors\n"
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


def build_mtech_case_branch_website_payload(wa_id: str):
    """Builds a well-formatted WhatsApp text payload for M.Tech CASE information."""

    text = (
        "🏗️💻 *GM University – M.Tech Computer Aided Structural Engineering*\n\n"

        "📌 Official website/link will be updated soon.\n\n"

        "Stay connected with GM University for updates regarding:\n"
        "━━━━━━━━━━━━━━━\n"
        "• Program Overview\n"
        "• Curriculum Details\n"
        "• Practical Training\n"
        "• Structural Engineering Lab Learning\n"
        "• CAD and Simulation Projects\n"
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
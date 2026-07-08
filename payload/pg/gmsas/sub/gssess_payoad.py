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

def build_mtech_sesse_program_payload(wa_id: str):
    """Builds the payload for the M.Tech Smart Electrical Systems and Sustainable Energy program."""

    header = MessageHeader(
        text="⚡🌱 M.Tech Smart Electrical Systems and Sustainable Energy"
    )

    body = MessageBody(
        text=(
            "🎓 *M.Tech in Smart Electrical Systems and Sustainable Energy*\n\n"
            "Learn core concepts in:\n"
            "• Smart Electrical Systems\n"
            "• Sustainable Energy Technologies\n"
            "• Renewable Energy Systems\n"
            "• Smart Grid Technologies\n"
            "• Power Electronics\n"
            "• Energy Storage Systems\n"
            "• Electric Vehicles and Charging Systems\n"
            "• Power System Automation\n"
            "• Energy Management Systems\n"
            "• Green Energy and Sustainability\n\n"
            "Get details about the program, eligibility, curriculum, "
            "training, practical learning, and career opportunities.\n\n"
            "Please choose an option below 👇"
        )
    )

    footer = MessageFooter(
        text="🎓 GM University Admissions 2026-27"
    )

    btn_program_details = Button(reply=ButtonReply(id="baaea", title="Program Details"))
    btn_fee_duration = Button(reply=ButtonReply(id="baaeb", title="Fee Details"))
    btn_branch_website = Button(reply=ButtonReply(id="baaec", title="More Info"))

    action = ButtonAction(buttons=[btn_program_details, btn_fee_duration, btn_branch_website])

    interactive = InteractiveButton(
        header=header,
        body=body,
        footer=footer,
        action=action,
    )

    payload = WhatsAppInteractiveButtonRequest(to=wa_id, interactive=interactive)
    return payload.model_dump()


def build_mtech_sesse_program_details_payload(wa_id: str):
    """Builds a well-formatted WhatsApp text payload for full M.Tech Smart Electrical Systems and Sustainable Energy program details."""

    text = (
        "🎓 *M.Tech in Smart Electrical Systems and Sustainable Energy*\n"
        "📘 *Program Details – 2026-27 Intake*\n\n"

        "━━━━━━━━━━━━━━━\n"
        "📄 *Program Document Includes:*\n"
        "• Curriculum Structure\n"
        "• Eligibility Criteria\n"
        "• Smart Electrical Systems Core Subjects\n"
        "• Sustainable Energy Concepts\n"
        "• Practical & Industry-Oriented Learning\n"
        "• Academic & Career Opportunities\n"
        "━━━━━━━━━━━━━━━\n\n"

        "🔗 *View Full Program Document:*\n"
        "https://gmu.ac.in/imgview?dummy=data2024&base=assets%2Fdownloadmaterial%2FGMU%20School%20of%20Advanced%20%20Studies%20%20Pdf%20Final%2FM.%20Tech.%20in%20Smart%20Electrical%20Systems%20and%20Sustainable%20Energy%20-%20Program%20Document%2FM.%20Tech.%20in%20Smart%20Electrical%20Systems%20and%20Sustainable%20Energy%20-%20Program%20Document-&ext=png"
        "\n\n📞 *Contact Details*\n"
        "━━━━━━━━━━━━━━━\n"
        "📍 GM University, Davangere\n"
        "☎️ Phone: +91 9364099712,+91 9364099720\n"
        # "📧 Email: mtech.sesse@gmu.ac.in\n"
    )

    payload = WhatsAppTextReplyRequest(
        to=wa_id,
        text=TextBody(
            body=text,
            preview_url=True
        ),
    )

    return payload.model_dump()


def build_mtech_sesse_fee_duration_payload(wa_id: str):
    """Builds a well-formatted WhatsApp text payload for M.Tech Smart Electrical Systems and Sustainable Energy fee information."""

    text = (
        "🎓 *GM University – M.Tech Smart Electrical Systems and Sustainable Energy Fee Details*\n\n"

        "📌 Fee details\n"
        "━━━━━━━━━━━━━━━\n"
        "₹1,25,000\n\n"

        "⏳ *Program Duration*\n"
        "━━━━━━━━━━━━━━━\n"
        "2 Years \n\n"

        "📘 *Program Information:*\n"
        "━━━━━━━━━━━━━━━\n"
        "• Advanced smart electrical systems focused program\n"
        "• Renewable and sustainable energy learning\n"
        "• Smart grid and energy management practical training\n"
        "• Industry-oriented electrical and power systems concepts\n"
        "• Career opportunities in energy, power systems and sustainability sectors\n"
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


def build_mtech_sesse_branch_website_payload(wa_id: str):
    """Builds a well-formatted WhatsApp text payload for M.Tech Smart Electrical Systems and Sustainable Energy information."""

    text = (
        "⚡🌱 *GM University – M.Tech Smart Electrical Systems and Sustainable Energy*\n\n"

        "📌 Official website/link will be updated soon.\n\n"

        "Stay connected with GM University for updates regarding:\n"
        "━━━━━━━━━━━━━━━\n"
        "• Program Overview\n"
        "• Curriculum Details\n"
        "• Practical Training\n"
        "• Smart Grid Lab Learning\n"
        "• Sustainable Energy Projects\n"
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
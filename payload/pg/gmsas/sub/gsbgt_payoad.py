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

def build_mtech_bgt_program_payload(wa_id: str):
    """Builds the payload for the M.Tech Bioengineering and Genetic Technology program."""

    header = MessageHeader(
        text="🧬🔬 M.Tech Bioengineering and Genetic Technology"
    )

    body = MessageBody(
        text=(
            "🎓 *M.Tech in Bioengineering and Genetic Technology*\n\n"
            "Learn core concepts in:\n"
            "• Bioengineering Principles\n"
            "• Genetic Engineering\n"
            "• Molecular Biology\n"
            "• Biotechnology\n"
            "• Cell and Tissue Engineering\n"
            "• Genomics and Proteomics\n"
            "• Bioinformatics\n"
            "• Bioprocess Technology\n"
            "• Biomedical Applications\n"
            "• Research Methods in Genetic Technology\n\n"
            "Get details about the program, eligibility, curriculum, "
            "training, practical learning, and career opportunities.\n\n"
            "Please choose an option below 👇"
        )
    )

    footer = MessageFooter(
        text="🎓 GM University Admissions 2026-27"
    )

    btn_program_details = Button(reply=ButtonReply(id="baaga", title="Program Details"))
    btn_fee_duration = Button(reply=ButtonReply(id="baagb", title="Fee Details"))
    btn_branch_website = Button(reply=ButtonReply(id="baagc", title="More Info"))

    action = ButtonAction(buttons=[btn_program_details, btn_fee_duration, btn_branch_website])

    interactive = InteractiveButton(
        header=header,
        body=body,
        footer=footer,
        action=action,
    )

    payload = WhatsAppInteractiveButtonRequest(to=wa_id, interactive=interactive)
    return payload.model_dump()


def build_mtech_bgt_program_details_payload(wa_id: str):
    """Builds a well-formatted WhatsApp text payload for full M.Tech Bioengineering and Genetic Technology program details."""

    text = (
        "🎓 *M.Tech in Bioengineering and Genetic Technology*\n"
        "📘 *Program Details – 2026-27 Intake*\n\n"

        "━━━━━━━━━━━━━━━\n"
        "📄 *Program Document Includes:*\n"
        "• Curriculum Structure\n"
        "• Eligibility Criteria\n"
        "• Bioengineering Core Subjects\n"
        "• Genetic Technology Concepts\n"
        "• Practical & Research-Oriented Learning\n"
        "• Academic & Career Opportunities\n"
        "━━━━━━━━━━━━━━━\n\n"

        "🔗 *View Full Program Document:*\n"
        "https://gmu.ac.in/imgview?dummy=data2024&base=assets%2Fdownloadmaterial%2FGMU%20School%20of%20Advanced%20%20Studies%20%20Pdf%20Final%2FM.%20Tech.%20in%20Bioengineering%20and%20Genetic%20Technology%20-%20Program%20Document%2FM.%20Tech.%20in%20Bioengineering%20and%20Genetic%20Technology%20-%20Program%20Document-&ext=png"
        "\n\n📞 *Contact Details*\n"
        "━━━━━━━━━━━━━━━\n"
        "📍 GM University, Davangere\n"
        "☎️ Phone: +91 9364099712,+91 9364099720\n"
        # "📧 Email: mtech.bgt@gmu.ac.in\n"
    )

    payload = WhatsAppTextReplyRequest(
        to=wa_id,
        text=TextBody(
            body=text,
            preview_url=True
        ),
    )

    return payload.model_dump()


def build_mtech_bgt_fee_duration_payload(wa_id: str):
    """Builds a well-formatted WhatsApp text payload for M.Tech Bioengineering and Genetic Technology fee information."""

    text = (
        "🎓 *GM University – M.Tech Bioengineering and Genetic Technology Fee Details*\n\n"

        "📌 Fee details\n"
        "━━━━━━━━━━━━━━━\n"
        "₹1,25,000\n\n"

        "⏳ *Program Duration*\n"
        "━━━━━━━━━━━━━━━\n"
        "2 Years \n\n"

        "📘 *Program Information:*\n"
        "━━━━━━━━━━━━━━━\n"
        "• Advanced bioengineering focused program\n"
        "• Genetic engineering and molecular biology learning\n"
        "• Biotechnology and biomedical application training\n"
        "• Research-oriented laboratory practicals\n"
        "• Career opportunities in biotech, healthcare, research and life sciences sectors\n"
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


def build_mtech_bgt_branch_website_payload(wa_id: str):
    """Builds a well-formatted WhatsApp text payload for M.Tech Bioengineering and Genetic Technology information."""

    text = (
        "🧬🔬 *GM University – M.Tech Bioengineering and Genetic Technology*\n\n"

        "📌 Official website/link will be updated soon.\n\n"

        "Stay connected with GM University for updates regarding:\n"
        "━━━━━━━━━━━━━━━\n"
        "• Program Overview\n"
        "• Curriculum Details\n"
        "• Practical Training\n"
        "• Bioengineering Lab Learning\n"
        "• Genetic Technology Projects\n"
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
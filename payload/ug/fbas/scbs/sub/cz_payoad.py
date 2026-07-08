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

def build_bsc_cz_program_payload(wa_id: str):
    """Builds the payload for the B.Sc Chemistry and Zoology program."""

    header = MessageHeader(
        text="🧪🧬 B.Sc Chemistry and Zoology"
    )

    body = MessageBody(
        text=(
            "🎓 *B.Sc Chemistry and Zoology*\n\n"
            "Learn core concepts in:\n"
            "• Physical Chemistry\n"
            "• Organic Chemistry\n"
            "• Inorganic Chemistry\n"
            "• Analytical Chemistry\n"
            "• Environmental Chemistry\n"
            "• Animal Diversity\n"
            "• Cell Biology\n"
            "• Genetics\n"
            "• Human Physiology\n"
            "• Ecology & Evolution\n\n"
            "Get details about the program, fee structure, placements, "
            "and department information.\n\n"
            "Please choose an option below 👇"
        )
    )

    footer = MessageFooter(
        text="🎓 GM University Admissions 2026-27"
    )

    btn_program_details = Button(reply=ButtonReply(id="adbca", title="Program Details"))
    btn_fee_duration = Button(reply=ButtonReply(id="adbcb", title="Fee & Duration"))
    btn_branch_website = Button(reply=ButtonReply(id="adbcc", title="Branch Website"))

    action = ButtonAction(buttons=[btn_program_details, btn_fee_duration, btn_branch_website])

    interactive = InteractiveButton(
        header=header,
        body=body,
        footer=footer,
        action=action,
    )

    payload = WhatsAppInteractiveButtonRequest(to=wa_id, interactive=interactive)
    return payload.model_dump()


def build_bsc_cz_program_details_payload(wa_id: str):
    """Builds a well-formatted WhatsApp text payload for full B.Sc Chemistry and Zoology program details."""

    text = (
        "🎓 *B.Sc Chemistry and Zoology*\n"
        "🏫 *School of Chemical and Biological Sciences*\n"
        "📘 *Program Details – 2026-27 Intake*\n\n"

        "━━━━━━━━━━━━━━━\n"
        "📄 *Program Brochure Includes:*\n"
        "• Curriculum Structure\n"
        "• Eligibility Criteria\n"
        "• Chemistry & Zoology Core Subjects\n"
        "• School Highlights\n"
        "• Academic & Career Opportunities\n"
        "━━━━━━━━━━━━━━━\n\n"

        "🔗 *View Full Program Brochure:*\n"
        "https://www.gmu.ac.in/pdfview_assets%5Cdownloadmaterial%5CSchool%20of%20Chemical%20and%20Biological%20Sciences-Program%20Docs%5CPD_SCBS_2026-27.pdf"

        "\n\n📞 *Contact Details*\n"
        "━━━━━━━━━━━━━━━\n"
        "📍 GM University, Davangere\n"
        "☎️ Phone: +91 9364099712,+91 9364099720\n"
        # "📧 Email: bsccz@gmu.ac.in\n"
    )

    payload = WhatsAppTextReplyRequest(
        to=wa_id,
        text=TextBody(
            body=text,
            preview_url=True
        ),
    )

    return payload.model_dump()


def build_bsc_cz_fee_duration_payload(wa_id: str):
    """Builds a well-formatted WhatsApp text payload for B.Sc Chemistry and Zoology fee and duration information."""

    text = (
        "🎓 *GM University – B.Sc Chemistry and Zoology Program Fee Details*\n\n"

        "🧪🧬 *Current B.Sc Chemistry and Zoology Fee*\n"
        "━━━━━━━━━━━━━━━\n"
        "Program Annual Fee ₹62,500\n\n"

        "⏳ *Program Duration*\n"
        "━━━━━━━━━━━━━━━\n"
        "3 Years \n\n"

        "📞 *Contact Details*\n"
        "━━━━━━━━━━━━━━━\n"
        "📍 GM University, Davangere\n"
        "☎️ Phone: +91 9364099712,+91 9364099720\n"
        # "📧 Email: bsccz@gmu.ac.in\n"
    )

    payload = WhatsAppTextReplyRequest(
        to=wa_id,
        text=TextBody(
            body=text,
            preview_url=False
        ),
    )

    return payload.model_dump()


def build_bsc_cz_branch_website_payload(wa_id: str):
    """Builds a well-formatted WhatsApp text payload for the School of Chemical and Biological Sciences website."""

    text = (
        "🧪🧬 *GM University – School of Chemical and Biological Sciences*\n\n"

        "🌐 Official website will be updated soon.\n\n"

        "📌 Stay connected with GM University for the latest updates regarding:\n"
        "━━━━━━━━━━━━━━━\n"
        "• School Overview\n"
        "• Programs & Curriculum\n"
        "• Faculty Information\n"
        "• Chemistry Laboratories\n"
        "• Zoology Laboratories\n"
        "• Events & Seminars\n"
        "• Placement Highlights\n"
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
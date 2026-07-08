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

def build_bsc_bte_program_payload(wa_id: str):
    """Builds the payload for the Biotechnology and Tissue Engineering program."""

    header = MessageHeader(
        text="🧬🔬 Biotechnology and Tissue Engineering"
    )

    body = MessageBody(
        text=(
            "🎓 *B.Sc Biotechnology and Tissue Engineering*\n\n"
            "Learn core concepts in:\n"
            "• Cell Biology\n"
            "• Molecular Biology\n"
            "• Genetics\n"
            "• Microbiology\n"
            "• Biotechnology Principles\n"
            "• Tissue Engineering\n"
            "• Stem Cell Technology\n"
            "• Bioprocess Technology\n"
            "• Immunology\n"
            "• Bioinformatics\n\n"
            "Get details about the program, fee structure, placements, "
            "and department information.\n\n"
            "Please choose an option below 👇"
        )
    )

    footer = MessageFooter(
        text="🎓 GM University Admissions 2026-27"
    )

    btn_program_details = Button(reply=ButtonReply(id="adcba", title="Program Details"))
    btn_fee_duration = Button(reply=ButtonReply(id="adcbb", title="Fee & Duration"))
    btn_branch_website = Button(reply=ButtonReply(id="adcbc", title="Branch Website"))

    action = ButtonAction(buttons=[btn_program_details, btn_fee_duration, btn_branch_website])

    interactive = InteractiveButton(
        header=header,
        body=body,
        footer=footer,
        action=action,
    )

    payload = WhatsAppInteractiveButtonRequest(to=wa_id, interactive=interactive)
    return payload.model_dump()


def build_bsc_bte_program_details_payload(wa_id: str):
    """Builds a well-formatted WhatsApp text payload for full Biotechnology and Tissue Engineering program details."""

    text = (
        "🎓 *B.Sc Biotechnology and Tissue Engineering*\n"
        "🏫 *School of Applied Sciences*\n"
        "📘 *Program Details – 2026-27 Intake*\n\n"

        "━━━━━━━━━━━━━━━\n"
        "📄 *Program Brochure Includes:*\n"
        "• Curriculum Structure\n"
        "• Eligibility Criteria\n"
        "• Biotechnology & Tissue Engineering Core Subjects\n"
        "• School Highlights\n"
        "• Academic & Career Opportunities\n"
        "━━━━━━━━━━━━━━━\n\n"

        "🔗 *View Full Program Brochure:*\n"
        "https://gmu.ac.in/pdfview_assets%5Cdownloadmaterial%5CSchool%20of%20Applied%20Sciences-%20Program%20Docs%5CB.Sc%20Biotechnology%20and%20Tissue%20engineering%20-Program%20Document%20%29%20final%202025%20Nov%20%281%29.pdf"

        "\n\n📞 *Contact Details*\n"
        "━━━━━━━━━━━━━━━\n"
        "📍 GM University, Davangere\n"
        "☎️ Phone: +91 9364099712,+91 9364099720\n"
        # "📧 Email: bscbte@gmu.ac.in\n"
    )

    payload = WhatsAppTextReplyRequest(
        to=wa_id,
        text=TextBody(
            body=text,
            preview_url=True
        ),
    )

    return payload.model_dump()


def build_bsc_bte_fee_duration_payload(wa_id: str):
    """Builds a well-formatted WhatsApp text payload for Biotechnology and Tissue Engineering fee and duration information."""

    text = (
        "🎓 *GM University – Biotechnology and Tissue Engineering Program Fee Details*\n\n"

        "🧬🔬 *Current Biotechnology and Tissue Engineering Fee*\n"
        "━━━━━━━━━━━━━━━\n"
        "Program Annual Fee ₹92,500\n\n"

        "⏳ *Program Duration*\n"
        "━━━━━━━━━━━━━━━\n"
        "3 Years \n\n"

        "📞 *Contact Details*\n"
        "━━━━━━━━━━━━━━━\n"
        "📍 GM University, Davangere\n"
        "☎️ Phone: +91 9364099712,+91 9364099720\n"
        # "📧 Email: bscbte@gmu.ac.in\n"
    )

    payload = WhatsAppTextReplyRequest(
        to=wa_id,
        text=TextBody(
            body=text,
            preview_url=False
        ),
    )

    return payload.model_dump()


def build_bsc_bte_branch_website_payload(wa_id: str):
    """Builds a well-formatted WhatsApp text payload for the School of Applied Sciences website."""

    text = (
        "🧬🔬 *GM University – School of Applied Sciences*\n\n"

        "🌐 Official website will be updated soon.\n\n"

        "📌 Stay connected with GM University for the latest updates regarding:\n"
        "━━━━━━━━━━━━━━━\n"
        "• School Overview\n"
        "• Programs & Curriculum\n"
        "• Faculty Information\n"
        "• Biotechnology Laboratories\n"
        "• Tissue Engineering Facilities\n"
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
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

def build_bsc_im_program_payload(wa_id: str):
    """Builds the payload for the Industrial Microbiology program."""

    header = MessageHeader(
        text="🦠🔬 Industrial Microbiology"
    )

    body = MessageBody(
        text=(
            "🎓 *B.Sc Industrial Microbiology*\n\n"
            "Learn core concepts in:\n"
            "• General Microbiology\n"
            "• Industrial Microbiology\n"
            "• Microbial Genetics\n"
            "• Fermentation Technology\n"
            "• Food Microbiology\n"
            "• Pharmaceutical Microbiology\n"
            "• Environmental Microbiology\n"
            "• Immunology\n"
            "• Bioprocess Technology\n"
            "• Microbial Quality Control\n\n"
            "Get details about the program, fee structure, placements, "
            "and department information.\n\n"
            "Please choose an option below 👇"
        )
    )

    footer = MessageFooter(
        text="🎓 GM University Admissions 2026-27"
    )

    btn_program_details = Button(reply=ButtonReply(id="adcca", title="Program Details"))
    btn_fee_duration = Button(reply=ButtonReply(id="adccb", title="Fee & Duration"))
    btn_branch_website = Button(reply=ButtonReply(id="adccc", title="Branch Website"))

    action = ButtonAction(buttons=[btn_program_details, btn_fee_duration, btn_branch_website])

    interactive = InteractiveButton(
        header=header,
        body=body,
        footer=footer,
        action=action,
    )

    payload = WhatsAppInteractiveButtonRequest(to=wa_id, interactive=interactive)
    return payload.model_dump()


def build_bsc_im_program_details_payload(wa_id: str):
    """Builds a well-formatted WhatsApp text payload for full Industrial Microbiology program details."""

    text = (
        "🎓 *B.Sc Industrial Microbiology*\n"
        "🏫 *School of Applied Sciences*\n"
        "📘 *Program Details – 2026-27 Intake*\n\n"

        "━━━━━━━━━━━━━━━\n"
        "📄 *Program Brochure Includes:*\n"
        "• Curriculum Structure\n"
        "• Eligibility Criteria\n"
        "• Industrial Microbiology Core Subjects\n"
        "• School Highlights\n"
        "• Academic & Career Opportunities\n"
        "━━━━━━━━━━━━━━━\n\n"

        "🔗 *View Full Program Brochure:*\n"
        "https://gmu.ac.in/pdfview_assets%5Cdownloadmaterial%5CSchool%20of%20Applied%20Sciences-%20Program%20Docs%5CB.Sc-%20Industrial%20Microbiology%20-Program%20document.pdf"

        "\n\n📞 *Contact Details*\n"
        "━━━━━━━━━━━━━━━\n"
        "📍 GM University, Davangere\n"
        "☎️ Phone: +91 9364099712,+91 9364099720\n"
        # "📧 Email: bscim@gmu.ac.in\n"
    )

    payload = WhatsAppTextReplyRequest(
        to=wa_id,
        text=TextBody(
            body=text,
            preview_url=True
        ),
    )

    return payload.model_dump()


def build_bsc_im_fee_duration_payload(wa_id: str):
    """Builds a well-formatted WhatsApp text payload for Industrial Microbiology fee and duration information."""

    text = (
        "🎓 *GM University – Industrial Microbiology Program Fee Details*\n\n"

        "🦠🔬 *Current Industrial Microbiology Fee*\n"
        "━━━━━━━━━━━━━━━\n"
        "Program Annual Fee ₹92,500\n\n"

        "⏳ *Program Duration*\n"
        "━━━━━━━━━━━━━━━\n"
        "3 Years \n\n"

        "📞 *Contact Details*\n"
        "━━━━━━━━━━━━━━━\n"
        "📍 GM University, Davangere\n"
        "☎️ Phone: +91 9364099712,+91 9364099720\n"
        # "📧 Email: bscim@gmu.ac.in\n"
    )

    payload = WhatsAppTextReplyRequest(
        to=wa_id,
        text=TextBody(
            body=text,
            preview_url=False
        ),
    )

    return payload.model_dump()


def build_bsc_im_branch_website_payload(wa_id: str):
    """Builds a well-formatted WhatsApp text payload for the School of Applied Sciences website."""

    text = (
        "🦠🔬 *GM University – School of Applied Sciences*\n\n"

        "🌐 Official website will be updated soon.\n\n"

        "📌 Stay connected with GM University for the latest updates regarding:\n"
        "━━━━━━━━━━━━━━━\n"
        "• School Overview\n"
        "• Programs & Curriculum\n"
        "• Faculty Information\n"
        "• Microbiology Laboratories\n"
        "• Fermentation & Bioprocess Facilities\n"
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
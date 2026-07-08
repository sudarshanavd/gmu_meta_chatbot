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

def build_bcomllb_program_payload(wa_id: str):
    """Builds the payload for the B.Com., LL.B. Integrated program."""

    header = MessageHeader(
        text="⚖️ B.Com., LL.B. (Integrated)"
    )

    body = MessageBody(
        text=(
            "🎓 *B.Com., LL.B. (Integrated)*\n\n"
            "Learn core concepts in:\n"
            "• Financial Accounting\n"
            "• Business Law\n"
            "• Constitutional Law\n"
            "• Contract Law\n"
            "• Corporate Law\n"
            "• Taxation Law\n"
            "• Criminal Law\n"
            "• Family Law\n"
            "• Legal Research & Writing\n"
            "• Moot Court & Legal Practice\n\n"
            "Get details about the program, fee structure, placements, "
            "and department information.\n\n"
            "Please choose an option below 👇"
        )
    )

    footer = MessageFooter(
        text="🎓 GM University Admissions 2026-27"
    )

    btn_program_details = Button(reply=ButtonReply(id="accaa", title="Program Details"))
    btn_fee_duration = Button(reply=ButtonReply(id="accab", title="Fee & Duration"))
    btn_branch_website = Button(reply=ButtonReply(id="accac", title="Branch Website"))

    action = ButtonAction(buttons=[btn_program_details, btn_fee_duration, btn_branch_website])

    interactive = InteractiveButton(
        header=header,
        body=body,
        footer=footer,
        action=action,
    )

    payload = WhatsAppInteractiveButtonRequest(to=wa_id, interactive=interactive)
    return payload.model_dump()


def build_bcomllb_program_details_payload(wa_id: str):
    """Builds a well-formatted WhatsApp text payload for full B.Com., LL.B. Integrated program details."""

    text = (
        "🎓 *B.Com., LL.B. (Integrated)*\n"
        "📘 *Program Details – 2026-27 Intake*\n\n"

        "━━━━━━━━━━━━━━━\n"
        "📄 *Program Brochure Includes:*\n"
        "• Curriculum Structure\n"
        "• Eligibility Criteria\n"
        "• Commerce & Legal Studies Core Subjects\n"
        "• Faculty Highlights\n"
        "• Academic & Career Opportunities\n"
        "━━━━━━━━━━━━━━━\n\n"

        "🔗 *View Full Program Brochure:*\n"
        "http://gmu.ac.in/pdfview_assets%5Cdownloadmaterial%5CFaculty%20of%20Legal%20Studies%20and%20Public%20Policy%5CPD_BComLLB_2026-27.pdf"
        "\n\n📞 *Contact Details*\n"
        "━━━━━━━━━━━━━━━\n"
        "📍 GM University, Davangere\n"
        "☎️ Phone: +91 9364099712,+91 9364099720\n"
        # "📧 Email: bcomllb@gmu.ac.in\n"
    )

    payload = WhatsAppTextReplyRequest(
        to=wa_id,
        text=TextBody(
            body=text,
            preview_url=True
        ),
    )

    return payload.model_dump()


def build_bcomllb_fee_duration_payload(wa_id: str):
    """Builds a well-formatted WhatsApp text payload for B.Com., LL.B. Integrated fee and duration information."""

    text = (
        "🎓 *GM University – B.Com., LL.B. Integrated Program Fee Details*\n\n"

        "⚖️ *Current B.Com., LL.B. Fee*\n"
        "━━━━━━━━━━━━━━━\n"
        "₹1,02,500 per year\n"

        "⏳ *Program Duration*\n"
        "━━━━━━━━━━━━━━━\n"
        "3 Years \n\n"

        "📞 *Contact Details*\n"
        "━━━━━━━━━━━━━━━\n"
        "📍 GM University, Davangere\n"
        "☎️ Phone: +91 9364099712,+91 9364099720\n"
        # "📧 Email: bcomllb@gmu.ac.in\n"
    )

    payload = WhatsAppTextReplyRequest(
        to=wa_id,
        text=TextBody(
            body=text,
            preview_url=False
        ),
    )

    return payload.model_dump()


def build_bcomllb_branch_website_payload(wa_id: str):
    """Builds a well-formatted WhatsApp text payload for the B.Com., LL.B. Integrated branch website."""

    text = (
        "⚖️ *GM University – B.Com., LL.B. (Integrated)*\n\n"

        "🌐 Official website will be updated soon.\n\n"

        "📌 Stay connected with GM University for the latest updates regarding:\n"
        "━━━━━━━━━━━━━━━\n"
        "• Faculty Overview\n"
        "• Programs & Curriculum\n"
        "• Faculty Information\n"
        "• Moot Court Activities\n"
        "• Legal Aid Activities\n"
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
from schema.service_schema import (WhatsAppInteractiveButtonRequest, 
                                   InteractiveButton, 
                                   MessageBody, MessageHeader, 
                                   MessageFooter, ButtonAction,
                                   Button,ButtonReply,
                                   WhatsAppTextReplyRequest, TextBody
)

def build_ise_program_payload(wa_id: str):
    """Builds the payload for the Information Science and Engineering."""

    header = MessageHeader(
        text="💻Information Science and Engineering "
    )

    body = MessageBody(
        text=(
            "🎓 *B.Tech in Information Science & Engineering (ISE)*\n\n"
"Learn core concepts in:\n"
"• Information Systems\n"
"• Database Management\n"
"• Software Development\n"
"• Computer Networks\n"
"• Data Analytics\n"
"• Cyber Security Basics\n"
"• Cloud Computing\n"
"• Artificial Intelligence\n\n"
"Get details about the program, fee structure, placements, "
"and department information.\n\n"
"Please choose an option below 👇"
        )
    )

    footer = MessageFooter(
        text="🎓 GM University Admissions 2026-27"
    )

    btn_program_details = Button(reply=ButtonReply(id="aaaba", title="Program Details"))
    btn_fee_duration = Button(reply=ButtonReply(id="aaabb", title="Fee & Duration"))
    btn_branch_website = Button(reply=ButtonReply(id="aaabc", title="Branch Website"))

    action = ButtonAction(buttons=[btn_program_details, btn_fee_duration, btn_branch_website])

    interactive = InteractiveButton(
        header=header,
        body=body,
        footer=footer,
        action=action,
    )

    payload = WhatsAppInteractiveButtonRequest(to=wa_id, interactive=interactive)
    return payload.model_dump()


def build_ise_program_details_payload(wa_id: str):
    """Builds a well-formatted WhatsApp text payload for full CSE program details."""

    text = (
        "🎓 *B.TechInformation Science and Engineering (ISE)*\n"
        "📘 *Program Details – 2026-27 Intake*\n\n"

        "━━━━━━━━━━━━━━━\n"
        "📄 *Program Brochure Includes:*\n"
        "• Curriculum Structure\n"
        "• Eligibility Criteria\n"
        "• CSE Specializations\n"
        "• Department Highlights\n"
        "• Academic & Career Opportunities\n"
        "━━━━━━━━━━━━━━━\n\n"

        "🔗 *View Full Program Brochure:*\n"
        "https://gmu.ac.in/pdfview_assets%5Cdownloadmaterial%5CUG%20Programs%5Cprogram%5CPD_ISE_2026-27.pdf"
        "\n\n📞 *Contact Details*\n"
        "━━━━━━━━━━━━━━━\n"
        "📍 GM University, Davangere\n"
        "☎️ Phone: +91 9364099712,+91 9364099720\n"
        "📧 Email: hod.ise@gmu.ac.in\n"
    )

    payload = WhatsAppTextReplyRequest(
        to=wa_id,
        text=TextBody(
            body=text,
            preview_url=True
        ),
    )

    return payload.model_dump()


def build_ise_fee_duration_payload(wa_id: str):
    """Builds a well-formatted WhatsApp text payload for ISE fee and duration information."""

    text = (
        "🎓 *GM University – ISE Program Fee Details*\n\n"

        "⏱ *Duration:* 4 Years\n"
        "💻 *Current ISE Fee*\n"
        "━━━━━━━━━━━━━━━\n"
        "₹2,25,000 per year\n\n"

        "📞 *Contact Details*\n"
        "━━━━━━━━━━━━━━━\n"
        "📍 GM University, Davangere\n"
        "☎️ Phone: +91 9364099712,+91 9364099720\n"
        "📧 Email: hod.ise@gmu.ac.in\n"
    )

    payload = WhatsAppTextReplyRequest(
        to=wa_id,
        text=TextBody(
            body=text,
            preview_url=True
        ),
    )

    return payload.model_dump()


def build_ise_branch_website_payload(wa_id: str):
    """Builds a well-formatted WhatsApp text payload for the ISE branch website."""

    text = (
        "💻 *GM University – Information Science & Engineering*\n\n"

        "🌐 Explore the official ISE branch website for:\n"
        "━━━━━━━━━━━━━━━\n"
        "• Department Overview\n"
        "• Programs & Specializations\n"
        "• Faculty Information\n"
        "• Events & Activities\n"
        "• Placement Highlights\n"
        "• Student Resources\n"
        "━━━━━━━━━━━━━━━\n\n"

        "🔗 *Visit Website:*\n"
        "https://ise-website-rcxt.vercel.app//"
    )

    payload = WhatsAppTextReplyRequest(
        to=wa_id,
        text=TextBody(
            body=text,
            preview_url=True
        ),
    )

    return payload.model_dump()
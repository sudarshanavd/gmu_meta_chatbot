from schema.service_schema import (WhatsAppInteractiveButtonRequest, 
                                   InteractiveButton, 
                                   MessageBody, MessageHeader, 
                                   MessageFooter, ButtonAction,
                                   Button,ButtonReply,
                                   WhatsAppTextReplyRequest, TextBody
)

def build_iot_program_payload(wa_id: str):
    """Builds the payload for theComputer Science - IOT with AI."""

    header = MessageHeader(
        text="💻 Computer Science - IOT with AI"
    )

    body = MessageBody(
        text=(
           "🤖 *B.Tech in Computer Science - IoT with AI (IoT & AI)*\n\n"
"Learn core concepts in:\n"
"• Internet of Things (IoT)\n"
"• Artificial Intelligence (AI)\n"
"• Machine Learning\n"
"• Embedded Systems\n"
"• Sensor Networks\n"
"• Edge Computing\n"
"• Data Analytics\n"
"• Cloud Computing\n"
"• Computer Vision\n"
"• Robotics & Automation\n"
"• Smart Devices & Applications\n"
"• AI-Driven IoT Solutions\n\n"
"Gain practical skills in developing intelligent connected systems, "
"analyzing real-time data, and building smart applications for modern industries.\n\n"
"Get details about the program, fee structure, placements, "
"and department information.\n\n"
"Please choose an option below 👇"
        )
    )

    footer = MessageFooter(
        text="🎓 GM University Admissions 2026-27"
    )

    btn_program_details = Button(reply=ButtonReply(id="aaaea", title="Program Details"))
    btn_fee_duration = Button(reply=ButtonReply(id="aaaeb", title="Fee & Duration"))
    btn_branch_website = Button(reply=ButtonReply(id="aaaec", title="Branch Website"))

    action = ButtonAction(buttons=[btn_program_details, btn_fee_duration, btn_branch_website])

    interactive = InteractiveButton(
        header=header,
        body=body,
        footer=footer,
        action=action,
    )

    payload = WhatsAppInteractiveButtonRequest(to=wa_id, interactive=interactive)
    return payload.model_dump()


def build_iot_program_details_payload(wa_id: str):
    """Builds a well-formatted WhatsApp text payload for full CSE program details."""

    text = (
        "🎓 *B.Tech Computer Science - IOT with AI(IOT)*\n"
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
        "https://www.gmu.ac.in/pdfview_assets%5Cdownloadmaterial%5CUG%20Programs%5Cpd%5CPD_CSE_2026-27.pdf"
        "\n\n📞 *Contact Details*\n"
        "━━━━━━━━━━━━━━━\n"
        "📍 GM University, Davangere\n"
        "☎️ Phone: +91 9364099712,+91 9364099720\n"
        "📧 Email: hod.dsiot@gmu.ac.in\n"
    )

    payload = WhatsAppTextReplyRequest(
        to=wa_id,
        text=TextBody(
            body=text,
            preview_url=True
        ),
    )

    return payload.model_dump()


def build_iot_fee_duration_payload(wa_id: str):
    """Builds a well-formatted WhatsApp text payload for IOT fee and duration information."""

    text = (
        "🎓 *GM University – Computer Science - IOT with AI*\n\n"

        "⏱ *Duration:* 4 Years\n"
        "💻 *Current IOT Fee*\n"
        "━━━━━━━━━━━━━━━\n"
        "₹2,25,000 per year\n\n"

        "📞 *Contact Details*\n"
        "━━━━━━━━━━━━━━━\n"
        "📍 GM University, Davangere\n"
        "☎️ Phone: +91 9364099712,+91 9364099720\n"
        "📧 Email: hod.dsiot@gmu.ac.in\n"
    )

    payload = WhatsAppTextReplyRequest(
        to=wa_id,
        text=TextBody(
            body=text,
            preview_url=True
        ),
    )

    return payload.model_dump()


def build_iot_branch_website_payload(wa_id: str):
    """Builds a well-formatted WhatsApp text payload for the IOT branch website."""

    text = (
        "💻 *GM University – Computer Science - IOT with AI*\n\n"

        "🌐 Explore the official IOT branch website for:\n"
        "━━━━━━━━━━━━━━━\n"
        "• Department Overview\n"
        "• Programs & Specializations\n"
        "• Faculty Information\n"
        "• Events & Activities\n"
        "• Placement Highlights\n"
        "• Student Resources\n"
        "━━━━━━━━━━━━━━━\n\n"

        "🔗 *Visit Website:*\n"
        "https://gmu.ac.in/data_science//"
    )

    payload = WhatsAppTextReplyRequest(
        to=wa_id,
        text=TextBody(
            body=text,
            preview_url=True
        ),
    )

    return payload.model_dump()
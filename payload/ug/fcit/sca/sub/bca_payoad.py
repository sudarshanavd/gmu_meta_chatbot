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

def build_bca_general_program_payload(wa_id: str):
    """Builds the payload for the BCA General program."""

    header = MessageHeader(
        text="💻 BCA General"
    )

    body = MessageBody(
        text=(
            "🎓 *BCA General*\n\n"
            "Learn core concepts in:\n"
            "• Programming Fundamentals\n"
            "• Data Structures\n"
            "• Database Management Systems\n"
            "• Operating Systems\n"
            "• Computer Networks\n"
            "• Web Technologies\n"
            "• Software Engineering\n"
            "• Object-Oriented Programming\n"
            "• Cloud Computing Basics\n"
            "• Mobile Application Development\n\n"
            "Get details about the program, fee structure, placements, "
            "and department information.\n\n"
            "Please choose an option below 👇"
        )
    )

    footer = MessageFooter(
        text="🎓 GM University Admissions 2026-27"
    )

    btn_program_details = Button(reply=ButtonReply(id="aeaaa", title="Program Details"))
    btn_fee_duration = Button(reply=ButtonReply(id="aeaab", title="Fee & Duration"))
    btn_branch_website = Button(reply=ButtonReply(id="aeaac", title="Branch Website"))

    action = ButtonAction(buttons=[btn_program_details, btn_fee_duration, btn_branch_website])

    interactive = InteractiveButton(
        header=header,
        body=body,
        footer=footer,
        action=action,
    )

    payload = WhatsAppInteractiveButtonRequest(to=wa_id, interactive=interactive)
    return payload.model_dump()


def build_bca_general_program_details_payload(wa_id: str):
    """Builds a well-formatted WhatsApp text payload for full BCA General program details."""

    text = (
        "🎓 *BCA General*\n"
        "🏫 *School of Computer Applications*\n"
        "📘 *Program Details – 2026-27 Intake*\n\n"

        "━━━━━━━━━━━━━━━\n"
        "📄 *Program Brochure Includes:*\n"
        "• Curriculum Structure\n"
        "• Eligibility Criteria\n"
        "• Computer Applications Core Subjects\n"
        "• School Highlights\n"
        "• Academic & Career Opportunities\n"
        "━━━━━━━━━━━━━━━\n\n"

        "🔗 *View Full Program Brochure:*\n"
        "https://gmu.ac.in/pdfview_assets%5Cdownloadmaterial%5CSchool%20of%20Computer%20Applications-Program%20Docs%5CBCA%20Program%20Document%202025.pdf"

        "\n\n📞 *Contact Details*\n"
        "━━━━━━━━━━━━━━━\n"
        "📍 GM University, Davangere\n"
        "☎️ Phone: +91 9364099712,+91 9364099720\n"
        # "📧 Email: bca@gmu.ac.in\n"
    )

    payload = WhatsAppTextReplyRequest(
        to=wa_id,
        text=TextBody(
            body=text,
            preview_url=True
        ),
    )

    return payload.model_dump()


def build_bca_general_fee_duration_payload(wa_id: str):
    """Builds a well-formatted WhatsApp text payload for BCA General fee and duration information."""

    text = (
        "🎓 *GM University – BCA General Program Fee Details*\n\n"

        "💻 *Current BCA General Fee*\n"
        "━━━━━━━━━━━━━━━\n"
        "Program Annual Fee ₹1,02,500\n\n"

        "⏳ *Program Duration*\n"
        "━━━━━━━━━━━━━━━\n"
        "3 Years \n\n"

        "📞 *Contact Details*\n"
        "━━━━━━━━━━━━━━━\n"
        "📍 GM University, Davangere\n"
        "☎️ Phone: +91 9364099712,+91 9364099720\n"
        # "📧 Email: bca@gmu.ac.in\n"
    )

    payload = WhatsAppTextReplyRequest(
        to=wa_id,
        text=TextBody(
            body=text,
            preview_url=False
        ),
    )

    return payload.model_dump()


def build_bca_general_branch_website_payload(wa_id: str):
    """Builds a well-formatted WhatsApp text payload for the School of Computer Applications website."""

    text = (
        "💻 *GM University – School of Computer Applications*\n\n"

        "🌐 Official website will be updated soon.\n\n"

        "📌 Stay connected with GM University for the latest updates regarding:\n"
        "━━━━━━━━━━━━━━━\n"
        "• School Overview\n"
        "• Programs & Curriculum\n"
        "• Faculty Information\n"
        "• Computer Labs\n"
        "• Programming & Application Development\n"
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
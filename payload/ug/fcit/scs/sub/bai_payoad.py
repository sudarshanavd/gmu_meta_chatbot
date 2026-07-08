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

def build_bca_ai_data_analytics_program_payload(wa_id: str):
    """Builds the payload for the BCA AI and Data Analytics program."""

    header = MessageHeader(
        text="🤖📈 BCA AI and Data Analytics"
    )

    body = MessageBody(
        text=(
            "🎓 *BCA AI and Data Analytics*\n\n"
            "Learn core concepts in:\n"
            "• Programming Fundamentals\n"
            "• Database Management Systems\n"
            "• Data Structures\n"
            "• Operating Systems\n"
            "• Computer Networks\n"
            "• Artificial Intelligence Fundamentals\n"
            "• Data Analytics\n"
            "• Machine Learning Basics\n"
            "• Data Visualization\n"
            "• Python for Data Science\n"
            "• Business Intelligence\n"
            "• Predictive Analytics\n\n"
            "Get details about the program, fee structure, placements, "
            "and department information.\n\n"
            "Please choose an option below 👇"
        )
    )

    footer = MessageFooter(
        text="🎓 GM University Admissions 2026-27"
    )

    btn_program_details = Button(
        reply=ButtonReply(id="aebca", title="Program Details")
    )

    btn_fee_duration = Button(
        reply=ButtonReply(id="aebcb", title="Fee & Duration")
    )

    btn_branch_website = Button(
        reply=ButtonReply(id="aebcc", title="Branch Website")
    )

    action = ButtonAction(
        buttons=[
            btn_program_details,
            btn_fee_duration,
            btn_branch_website
        ]
    )

    interactive = InteractiveButton(
        header=header,
        body=body,
        footer=footer,
        action=action,
    )

    payload = WhatsAppInteractiveButtonRequest(
        to=wa_id,
        interactive=interactive
    )

    return payload.model_dump()

def build_bca_ai_data_analytics_program_details_payload(wa_id: str):
    """Builds a well-formatted WhatsApp text payload for full BCA AI and Data Analytics program details."""

    text = (
        "🎓 *BCA AI and Data Analytics*\n"
        "🏫 *School of Computer Science*\n"
        "📘 *Program Details – 2026-27 Intake*\n\n"

        "━━━━━━━━━━━━━━━\n"
        "📄 *Program Brochure Includes:*\n"
        "• Curriculum Structure\n"
        "• Eligibility Criteria\n"
        "• AI & Data Analytics Core Subjects\n"
        "• School Highlights\n"
        "• Academic & Career Opportunities\n"
        "━━━━━━━━━━━━━━━\n\n"

        "🔗 *View Full Program Brochure:*\n"
        "https://www.gmu.ac.in/pdfview_assets%5Cdownloadmaterial%5CSchool%20of%20Computer%20Science%20-Program%20Docs%5CPD_BCA-AIDA_2026-27.pdf"

        "\n\n📞 *Contact Details*\n"
        "━━━━━━━━━━━━━━━\n"
        "📍 GM University, Davangere\n"
        "☎️ Phone: +91 9364099712,+91 9364099720\n"
        # "📧 Email: bcaaida@gmu.ac.in\n"
    )

    payload = WhatsAppTextReplyRequest(
        to=wa_id,
        text=TextBody(
            body=text,
            preview_url=True
        ),
    )

    return payload.model_dump()

def build_bca_ai_data_analytics_fee_duration_payload(wa_id: str):
    """Builds a well-formatted WhatsApp text payload for BCA AI and Data Analytics fee and duration information."""

    text = (
        "🎓 *GM University – BCA AI and Data Analytics Program Fee Details*\n\n"

        "🤖📈 *Current BCA AI and Data Analytics Fee*\n"
        "━━━━━━━━━━━━━━━\n"
        "Program Annual Fee ₹1,02,500\n\n"
        
        "⏳ *Program Duration*\n"
        "━━━━━━━━━━━━━━━\n"
        "3 Years \n\n"

        "📞 *Contact Details*\n"
        "━━━━━━━━━━━━━━━\n"
        "📍 GM University, Davangere\n"
        "☎️ Phone: +91 9364099712,+91 9364099720\n"
        # "📧 Email: bcaaida@gmu.ac.in\n"
    )

    payload = WhatsAppTextReplyRequest(
        to=wa_id,
        text=TextBody(
            body=text,
            preview_url=False
        ),
    )

    return payload.model_dump()


def build_bca_cy_branch_website_payload(wa_id: str):
    """Builds a well-formatted WhatsApp text payload for the School of Computer Science website."""

    text = (
        "🔐💻 *GM University – School of Computer Science*\n\n"

        "🌐 Official website will be updated soon.\n\n"

        "📌 Stay connected with GM University for the latest updates regarding:\n"
        "━━━━━━━━━━━━━━━\n"
        "• School Overview\n"
        "• Programs & Curriculum\n"
        "• Faculty Information\n"
        "• Cyber Security Labs\n"
        "• Digital Forensics Facilities\n"
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
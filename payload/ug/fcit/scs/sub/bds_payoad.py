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

def build_bca_ds_program_payload(wa_id: str):
    """Builds the payload for the BCA Data Science program."""

    header = MessageHeader(
        text="📊💻 BCA Data Science"
    )

    body = MessageBody(
        text=(
            "🎓 *BCA Data Science*\n\n"
            "Learn core concepts in:\n"
            "• Programming Fundamentals\n"
            "• Python for Data Science\n"
            "• Data Structures\n"
            "• Database Management Systems\n"
            "• Statistics for Data Science\n"
            "• Data Analytics\n"
            "• Machine Learning\n"
            "• Data Visualization\n"
            "• Big Data Technologies\n"
            "• Artificial Intelligence Basics\n\n"
            "Get details about the program, fee structure, placements, "
            "and department information.\n\n"
            "Please choose an option below 👇"
        )
    )

    footer = MessageFooter(
        text="🎓 GM University Admissions 2026-27"
    )

    btn_program_details = Button(reply=ButtonReply(id="aebaa", title="Program Details"))
    btn_fee_duration = Button(reply=ButtonReply(id="aebab", title="Fee & Duration"))
    btn_branch_website = Button(reply=ButtonReply(id="aebac", title="Branch Website"))

    action = ButtonAction(buttons=[btn_program_details, btn_fee_duration, btn_branch_website])

    interactive = InteractiveButton(
        header=header,
        body=body,
        footer=footer,
        action=action,
    )

    payload = WhatsAppInteractiveButtonRequest(to=wa_id, interactive=interactive)
    return payload.model_dump()


def build_bca_ds_program_details_payload(wa_id: str):
    """Builds a well-formatted WhatsApp text payload for full BCA Data Science program details."""

    text = (
        "🎓 *BCA Data Science*\n"
        "🏫 *School of Computer Science*\n"
        "📘 *Program Details – 2026-27 Intake*\n\n"

        "━━━━━━━━━━━━━━━\n"
        "📄 *Program Brochure Includes:*\n"
        "• Curriculum Structure\n"
        "• Eligibility Criteria\n"
        "• Data Science Core Subjects\n"
        "• School Highlights\n"
        "• Academic & Career Opportunities\n"
        "━━━━━━━━━━━━━━━\n\n"

        "🔗 *View Full Program Brochure:*\n"
        "https://www.gmu.ac.in/pdfview_assets%5Cdownloadmaterial%5CSchool%20of%20Computer%20Science%20-Program%20Docs%5CPD_BCA-DS_2026-27_merged.pdf"

        "\n\n📞 *Contact Details*\n"
        "━━━━━━━━━━━━━━━\n"
        "📍 GM University, Davangere\n"
        "☎️ Phone: +91 9364099712,+91 9364099720\n"
        # "📧 Email: bcads@gmu.ac.in\n"
    )

    payload = WhatsAppTextReplyRequest(
        to=wa_id,
        text=TextBody(
            body=text,
            preview_url=True
        ),
    )

    return payload.model_dump()


def build_bca_ds_fee_duration_payload(wa_id: str):
    """Builds a well-formatted WhatsApp text payload for BCA Data Science fee and duration information."""

    text = (
        "🎓 *GM University – BCA Data Science Program Fee Details*\n\n"

        "📊💻 *Current BCA Data Science Fee*\n"
        "━━━━━━━━━━━━━━━\n"
        "Program Annual Fee ₹1,02,500\n\n"

        "⏳ *Program Duration*\n"
        "━━━━━━━━━━━━━━━\n"
        "3 Years \n\n"

        "📞 *Contact Details*\n"
        "━━━━━━━━━━━━━━━\n"
        "📍 GM University, Davangere\n"
        "☎️ Phone: +91 9364099712,+91 9364099720\n"
        # "📧 Email: bcads@gmu.ac.in\n"
    )

    payload = WhatsAppTextReplyRequest(
        to=wa_id,
        text=TextBody(
            body=text,
            preview_url=False
        ),
    )

    return payload.model_dump()


def build_bca_ds_branch_website_payload(wa_id: str):
    """Builds a well-formatted WhatsApp text payload for the School of Computer Science website."""

    text = (
        "📊💻 *GM University – School of Computer Science*\n\n"

        "🌐 Official website will be updated soon.\n\n"

        "📌 Stay connected with GM University for the latest updates regarding:\n"
        "━━━━━━━━━━━━━━━\n"
        "• School Overview\n"
        "• Programs & Curriculum\n"
        "• Faculty Information\n"
        "• Data Science Labs\n"
        "• Analytics & Machine Learning Facilities\n"
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
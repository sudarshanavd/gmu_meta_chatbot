
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

def build_bsc_scs_program_payload(wa_id: str):
    """Builds the payload for the B.Sc Statistics and Computer Science program."""

    header = MessageHeader(
        text="📊💻 B.Sc Statistics and Computer Science"
    )

    body = MessageBody(
        text=(
            "🎓 *B.Sc Statistics and Computer Science*\n\n"
            "Learn core concepts in:\n"
            "• Descriptive Statistics\n"
            "• Probability Theory\n"
            "• Statistical Inference\n"
            "• Regression Analysis\n"
            "• Sampling Techniques\n"
            "• Programming Fundamentals\n"
            "• Data Structures\n"
            "• Database Management Systems\n"
            "• Computer Networks\n"
            "• Data Analytics\n\n"
            "Get details about the program, fee structure, placements, "
            "and department information.\n\n"
            "Please choose an option below 👇"
        )
    )

    footer = MessageFooter(
        text="🎓 GM University Admissions 2026-27"
    )

    btn_program_details = Button(reply=ButtonReply(id="adaca", title="Program Details"))
    btn_fee_duration = Button(reply=ButtonReply(id="adacb", title="Fee & Duration"))
    btn_branch_website = Button(reply=ButtonReply(id="adacc", title="Branch Website"))

    action = ButtonAction(buttons=[btn_program_details, btn_fee_duration, btn_branch_website])

    interactive = InteractiveButton(
        header=header,
        body=body,
        footer=footer,
        action=action,
    )

    payload = WhatsAppInteractiveButtonRequest(to=wa_id, interactive=interactive)
    return payload.model_dump()


def build_bsc_scs_program_details_payload(wa_id: str):
    """Builds a well-formatted WhatsApp text payload for full B.Sc Statistics and Computer Science program details."""

    text = (
        "🎓 *B.Sc Statistics and Computer Science*\n"
        "🏫 *School of Mathematical and Physical Sciences*\n"
        "📘 *Program Details – 2026-27 Intake*\n\n"

        "━━━━━━━━━━━━━━━\n"
        "📄 *Program Brochure Includes:*\n"
        "• Curriculum Structure\n"
        "• Eligibility Criteria\n"
        "• Statistics & Computer Science Core Subjects\n"
        "• School Highlights\n"
        "• Academic & Career Opportunities\n"
        "━━━━━━━━━━━━━━━\n\n"

        "🔗 *View Full Program Brochure:*\n"
        "https://gmu.ac.in/pdfview_assets%5Cdownloadmaterial%5CSchool%20of%20Mathematical%20and%20Physical%20Sciences-Program%20Docs%5CSCs%20Course%20document%202025-2026.pdf"

        "📞 *Contact Details*\n"
        "━━━━━━━━━━━━━━━\n"
        "📍 GM University, Davangere\n"
        "☎️ Phone: +91 9364099712,+91 9364099720\n"
        # "📧 Email: bscscs@gmu.ac.in\n"
    )

    payload = WhatsAppTextReplyRequest(
        to=wa_id,
        text=TextBody(
            body=text,
            preview_url=True
        ),
    )

    return payload.model_dump()


def build_bsc_scs_fee_duration_payload(wa_id: str):
    """Builds a well-formatted WhatsApp text payload for B.Sc Statistics and Computer Science fee and duration information."""

    text = (
        "🎓 *GM University – B.Sc Statistics and Computer Science Program Fee Details*\n\n"

        "📊💻 *Current B.Sc Statistics and Computer Science Fee*\n"
        "━━━━━━━━━━━━━━━\n"
        "Program Annual Fee ₹62,500\n\n"

        "⏳ *Program Duration*\n"
        "━━━━━━━━━━━━━━━\n"
        "3 Years \n\n"

        "📞 *Contact Details*\n"
        "━━━━━━━━━━━━━━━\n"
        "📍 GM University, Davangere\n"
        "☎️ Phone: +91 9364099712,+91 9364099720\n"
        # "📧 Email: bscscs@gmu.ac.in\n"
    )

    payload = WhatsAppTextReplyRequest(
        to=wa_id,
        text=TextBody(
            body=text,
            preview_url=False
        ),
    )

    return payload.model_dump()


def build_bsc_scs_branch_website_payload(wa_id: str):
    """Builds a well-formatted WhatsApp text payload for the School of Mathematical and Physical Sciences website."""

    text = (
        "📊💻 *GM University – School of Mathematical and Physical Sciences*\n\n"

        "🌐 Official website will be updated soon.\n\n"

        "📌 Stay connected with GM University for the latest updates regarding:\n"
        "━━━━━━━━━━━━━━━\n"
        "• School Overview\n"
        "• Programs & Curriculum\n"
        "• Faculty Information\n"
        "• Statistics Learning Resources\n"
        "• Computer Science Labs\n"
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


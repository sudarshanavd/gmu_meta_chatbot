
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

def build_cs_aibcbs_program_payload(wa_id: str):
    """Builds the payload for the Computer Science - AI, Blockchain & Business Systems program."""

    header = MessageHeader(
        text="🤖⛓️💼 Computer Science - AI, Blockchain & Business Systems"
    )

    body = MessageBody(
        text=(
            "🎓 *B.Tech in Computer Science - AI, Blockchain & Business Systems (CS-AI, BC & BS)*\n\n"
            "Learn core concepts in:\n"
            "• Artificial Intelligence\n"
            "• Machine Learning\n"
            "• Blockchain Technology\n"
            "• Smart Contracts\n"
            "• Business Analytics\n"
            "• Data Science\n"
            "• Enterprise Systems\n"
            "• Financial Technologies (FinTech)\n"
            "• Cloud Computing\n"
            "• Digital Transformation\n\n"
            "Get details about the program, fee structure, placements, "
            "and department information.\n\n"
            "Please choose an option below 👇"
        )
    )

    footer = MessageFooter(
        text="🎓 GM University Admissions 2026-27"
    )

    btn_program_details = Button(reply=ButtonReply(id="aaada", title="Program Details"))
    btn_fee_duration = Button(reply=ButtonReply(id="aaadb", title="Fee & Duration"))
    btn_branch_website = Button(reply=ButtonReply(id="aaadc", title="Branch Website"))

    action = ButtonAction(buttons=[btn_program_details, btn_fee_duration, btn_branch_website])

    interactive = InteractiveButton(
        header=header,
        body=body,
        footer=footer,
        action=action,
    )

    payload = WhatsAppInteractiveButtonRequest(to=wa_id, interactive=interactive)
    return payload.model_dump()


def build_cs_aibcbs_program_details_payload(wa_id: str):
    """Builds a well-formatted WhatsApp text payload for full AI, Blockchain & Business Systems program details."""

    text = (
        "🎓 *B.Tech Computer Science - AI, Blockchain & Business Systems (CS-AI, BC & BS)*\n"
        "📘 *Program Details – 2026-27 Intake*\n\n"

        "━━━━━━━━━━━━━━━\n"
        "📄 *Program Brochure Includes:*\n"
        "• Curriculum Structure\n"
        "• Eligibility Criteria\n"
        "• AI, Blockchain & Business Systems Core Subjects\n"
        "• Department Highlights\n"
        "• Academic & Career Opportunities\n"
        "━━━━━━━━━━━━━━━\n\n"

        "🔗 *View Full Program Brochure:*\n"
        "https://gmu.ac.in/pdfview_assets%5Cdownloadmaterial%5CUG%20Programs%5Cprogram%5CPD_CC_2026-27.pdf"

        "\n\n📞 *Contact Details*\n"
        "━━━━━━━━━━━━━━━\n"
        "📍 GM University, Davangere\n"
        "☎️ Phone: +91 9364099712,+91 9364099720\n"
        "📧 Email: hod.bcbs@gmu.ac.in\n"
    )

    payload = WhatsAppTextReplyRequest(
        to=wa_id,
        text=TextBody(
            body=text,
            preview_url=True
        ),
    )

    return payload.model_dump()


def build_cs_aibcbs_fee_duration_payload(wa_id: str):
    """Builds a well-formatted WhatsApp text payload for AI, Blockchain & Business Systems fee and duration information."""

    text = (
        "🎓 *GM University – AI, Blockchain & Business Systems Program Fee Details*\n\n"

        "⏱ *Duration:* 4 Years\n"
        "🤖⛓️💼 *Current AI, Blockchain & Business Systems Fee*\n"
        "━━━━━━━━━━━━━━━\n"
        "₹2,25,000 per year\n\n"

        "📞 *Contact Details*\n"
        "━━━━━━━━━━━━━━━\n"
        "📍 GM University, Davangere\n"
        "☎️ Phone: +91 9364099712,+91 9364099720\n"
        "📧 Email: hod.bcbs@gmu.ac.in\n"
    )

    payload = WhatsAppTextReplyRequest(
        to=wa_id,
        text=TextBody(
            body=text,
            preview_url=True
        ),
    )

    return payload.model_dump()


def build_cs_aibcbs_branch_website_payload(wa_id: str):
    """Builds a well-formatted WhatsApp text payload for the AI, Blockchain & Business Systems branch website."""

    text = (
        "🤖⛓️💼 *GM University – Computer Science - AI, Blockchain & Business Systems*\n\n"

        "🌐 Explore the official branch website for:\n"
        "━━━━━━━━━━━━━━━\n"
        "• Department Overview\n"
        "• Programs & Curriculum\n"
        "• Faculty Information\n"
        "• AI, Blockchain & Innovation Labs\n"
        "• Events & Activities\n"
        "• Placement Highlights\n"
        "• Student Resources\n"
        "━━━━━━━━━━━━━━━\n\n"

        "🔗 *Visit Website:*\n"
        "https://gmu.ac.in/cc-bs/"
    )

    payload = WhatsAppTextReplyRequest(
        to=wa_id,
        text=TextBody(
            body=text,
            preview_url=True
        ),
    )

    return payload.model_dump()

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

def build_bca_cy_program_payload(wa_id: str):
    """Builds the payload for the BCA Cyber Security program."""

    header = MessageHeader(
        text="🔐💻 BCA Cyber Security"
    )

    body = MessageBody(
        text=(
            "🎓 *BCA Cyber Security*\n\n"
            "Learn core concepts in:\n"
            "• Programming Fundamentals\n"
            "• Computer Networks\n"
            "• Operating Systems\n"
            "• Database Management Systems\n"
            "• Information Security\n"
            "• Ethical Hacking\n"
            "• Network Security\n"
            "• Cryptography\n"
            "• Digital Forensics\n"
            "• Web Application Security\n\n"
            "Get details about the program, fee structure, placements, "
            "and department information.\n\n"
            "Please choose an option below 👇"
        )
    )

    footer = MessageFooter(
        text="🎓 GM University Admissions 2026-27"
    )

    btn_program_details = Button(reply=ButtonReply(id="aebba", title="Program Details"))
    btn_fee_duration = Button(reply=ButtonReply(id="aebbb", title="Fee & Duration"))
    btn_branch_website = Button(reply=ButtonReply(id="aebbc", title="Branch Website"))

    action = ButtonAction(buttons=[btn_program_details, btn_fee_duration, btn_branch_website])

    interactive = InteractiveButton(
        header=header,
        body=body,
        footer=footer,
        action=action,
    )

    payload = WhatsAppInteractiveButtonRequest(to=wa_id, interactive=interactive)
    return payload.model_dump()


def build_bca_cy_program_details_payload(wa_id: str):
    """Builds a well-formatted WhatsApp text payload for full BCA Cyber Security program details."""

    text = (
        "🎓 *BCA Cyber Security*\n"
        "🏫 *School of Computer Science*\n"
        "📘 *Program Details – 2026-27 Intake*\n\n"

        "━━━━━━━━━━━━━━━\n"
        "📄 *Program Brochure Includes:*\n"
        "• Curriculum Structure\n"
        "• Eligibility Criteria\n"
        "• Cyber Security Core Subjects\n"
        "• School Highlights\n"
        "• Academic & Career Opportunities\n"
        "━━━━━━━━━━━━━━━\n\n"

        "🔗 *View Full Program Brochure:*\n"
        "https://www.gmu.ac.in/pdfview_assets%5Cdownloadmaterial%5CSchool%20of%20Computer%20Science%20-Program%20Docs%5CPD_BCA-CY_2026-27.pdf"

        "\n\n📞 *Contact Details*\n"
        "━━━━━━━━━━━━━━━\n"
        "📍 GM University, Davangere\n"
        "☎️ Phone: +91 9364099712,+91 9364099720\n"
        # "📧 Email: bcacy@gmu.ac.in\n"
    )

    payload = WhatsAppTextReplyRequest(
        to=wa_id,
        text=TextBody(
            body=text,
            preview_url=True
        ),
    )

    return payload.model_dump()


def build_bca_cy_fee_duration_payload(wa_id: str):
    """Builds a well-formatted WhatsApp text payload for BCA Cyber Security fee and duration information."""

    text = (
        "🎓 *GM University – BCA Cyber Security Program Fee Details*\n\n"

        "🔐💻 *Current BCA Cyber Security Fee*\n"
        "━━━━━━━━━━━━━━━\n"
        "Program Annual Fee ₹1,02,500\n\n"

        "⏳ *Program Duration*\n"
        "━━━━━━━━━━━━━━━\n"
        "3 Years \n\n"

        "📞 *Contact Details*\n"
        "━━━━━━━━━━━━━━━\n"
        "📍 GM University, Davangere\n"
        "☎️ Phone: +91 9364099712,+91 9364099720\n"
        # "📧 Email: bcacy@gmu.ac.in\n"
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
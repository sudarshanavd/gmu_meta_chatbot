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

def build_phd_fet_program_payload(wa_id: str):
    """Builds the payload for the Ph.D Research Program under Faculty of Engineering and Technology."""

    header = MessageHeader(
        text="🎓 Ph.D Research Program"
    )

    body = MessageBody(
        text=(
            "🎓 *Ph.D Research Program*\n"
            "🏫 *Faculty of Engineering and Technology*\n\n"
            "Research areas include:\n"
            "• Computer Science and Engineering\n"
            "• Artificial Intelligence & Machine Learning\n"
            "• Cyber Security\n"
            "• Data Science\n"
            "• Electronics and Communication Engineering\n"
            "• Electrical and Electronics Engineering\n"
            "• Mechanical Engineering\n"
            "• Civil Engineering\n"
            "• Robotics and Automation\n"
            "• Emerging Technologies and Interdisciplinary Research\n\n"
            "Get details about research areas, eligibility, admission process, "
            "guides, facilities, and department information.\n\n"
            "Please choose an option below 👇"
        )
    )

    footer = MessageFooter(
        text="🎓 GM University Admissions 2026-27"
    )

    btn_program_details = Button(reply=ButtonReply(id="afaaa", title="Program Details"))
    btn_fee_duration = Button(reply=ButtonReply(id="afaab", title="Fee Details"))
    btn_branch_website = Button(reply=ButtonReply(id="afaac", title="More Info"))

    action = ButtonAction(buttons=[btn_program_details, btn_fee_duration, btn_branch_website])

    interactive = InteractiveButton(
        header=header,
        body=body,
        footer=footer,
        action=action,
    )

    payload = WhatsAppInteractiveButtonRequest(to=wa_id, interactive=interactive)
    return payload.model_dump()


def build_phd_fet_program_details_payload(wa_id: str):
    """Builds a well-formatted WhatsApp text payload for full Ph.D Research Program details."""

    text = (
        "🎓 *Ph.D Research Program*\n"
        "🏫 *Faculty of Engineering and Technology*\n"
        "📘 *Research Program Details – 2026-27 Intake*\n\n"

        "━━━━━━━━━━━━━━━\n"
        "📄 *Program Details Include:*\n"
        "• Research Areas\n"
        "• Eligibility Criteria\n"
        "• Admission Process\n"
        "• Research Supervisors\n"
        "• Laboratory & Research Facilities\n"
        "• Academic & Research Opportunities\n"
        "━━━━━━━━━━━━━━━\n\n"

        "🔬 *Research Focus Areas:*\n"
        "• Engineering and Technology\n"
        "• Computing and Artificial Intelligence\n"
        "• Cyber Security and Data Science\n"
        "• Electronics and Communication Systems\n"
        "• Mechanical, Civil and Electrical Engineering\n"
        "• Interdisciplinary and Applied Research\n\n"

        "📞 *Contact Details*\n"
        "━━━━━━━━━━━━━━━\n"
        "📍 GM University, Davangere\n"
        "☎️ Phone: +91 9364099712,+91 9364099720\n"
        # "📧 Email: phd.fet@gmu.ac.in\n"
    )

    payload = WhatsAppTextReplyRequest(
        to=wa_id,
        text=TextBody(
            body=text,
            preview_url=False
        ),
    )

    return payload.model_dump()


def build_phd_fet_fee_duration_payload(wa_id: str):
    """Builds a well-formatted WhatsApp text payload for Ph.D Research Program fee information."""

    text = (
        "🎓 *GM University – Ph.D Research Program Fee Details*\n\n"

        "📌 Fee details will be updated by the university admission office.\n\n"

        "📘 *For Ph.D Admission Information:*\n"
        "━━━━━━━━━━━━━━━\n"
        "• Research eligibility\n"
        "• Entrance/admission process\n"
        "• Supervisor availability\n"
        "• Department-wise research areas\n"
        "• University research guidelines\n"
        "━━━━━━━━━━━━━━━\n\n"

        "📞 *Contact Details*\n"
        "━━━━━━━━━━━━━━━\n"
        "📍 GM University, Davangere\n"
        "☎️ Phone:+91 9364099712,+91 9364099720\n"
        # "📧 Email: phd.fet@gmu.ac.in\n"
    )

    payload = WhatsAppTextReplyRequest(
        to=wa_id,
        text=TextBody(
            body=text,
            preview_url=False
        ),
    )

    return payload.model_dump()


def build_phd_fet_branch_website_payload(wa_id: str):
    """Builds a well-formatted WhatsApp text payload for Ph.D Research Program information."""

    text = (
        "🎓 *GM University – Ph.D Research Program*\n"
        "🏫 *Faculty of Engineering and Technology*\n\n"

        "📌 Official research program website/link will be updated soon.\n\n"

        "Stay connected with GM University for updates regarding:\n"
        "━━━━━━━━━━━━━━━\n"
        "• Research Admission Notifications\n"
        "• Research Areas\n"
        "• Supervisor Details\n"
        "• Department Research Facilities\n"
        "• Entrance Test / Interview Information\n"
        "• Important Dates\n"
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
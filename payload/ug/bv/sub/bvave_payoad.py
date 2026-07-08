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

def build_bsc_ave_program_payload(wa_id: str):
    """Builds the payload for the B.Sc Animation and Visual Effects program."""

    header = MessageHeader(
        text="🎬✨ B.Sc Animation and Visual Effects"
    )

    body = MessageBody(
        text=(
            "🎓 *B.Sc in Animation and Visual Effects*\n\n"
            "Learn core concepts in:\n"
            "• Animation Fundamentals\n"
            "• 2D Animation\n"
            "• 3D Animation\n"
            "• Visual Effects (VFX)\n"
            "• Digital Illustration\n"
            "• Storyboarding\n"
            "• Character Design\n"
            "• Motion Graphics\n"
            "• Video Editing\n"
            "• Compositing Techniques\n\n"
            "Get details about the program, eligibility, curriculum, "
            "training, practical learning, and career opportunities.\n\n"
            "Please choose an option below 👇"
        )
    )

    footer = MessageFooter(
        text="🎓 GM University Admissions 2026-27"
    )

    btn_program_details = Button(reply=ButtonReply(id="agafa", title="Program Details"))
    btn_fee_duration = Button(reply=ButtonReply(id="agafb", title="Fee Details"))
    btn_branch_website = Button(reply=ButtonReply(id="agafc", title="More Info"))

    action = ButtonAction(buttons=[btn_program_details, btn_fee_duration, btn_branch_website])

    interactive = InteractiveButton(
        header=header,
        body=body,
        footer=footer,
        action=action,
    )

    payload = WhatsAppInteractiveButtonRequest(to=wa_id, interactive=interactive)
    return payload.model_dump()


def build_bsc_ave_program_details_payload(wa_id: str):
    """Builds a well-formatted WhatsApp text payload for full B.Sc Animation and Visual Effects program details."""

    text = (
        "🎓 *B.Sc in Animation and Visual Effects*\n"
        "📘 *Program Details – 2026-27 Intake*\n\n"

        "━━━━━━━━━━━━━━━\n"
        "📄 *Program Document Includes:*\n"
        "• Curriculum Structure\n"
        "• Eligibility Criteria\n"
        "• Animation & VFX Core Subjects\n"
        "• Visual Design Training\n"
        "• Practical & Industry-Oriented Learning\n"
        "• Academic & Career Opportunities\n"
        "━━━━━━━━━━━━━━━\n\n"

        "🔗 *View Full Program Document:*\n"
        "https://gmu.ac.in/pdfview_assets%5Cdownloadmaterial%5CB%20Voc%20Programs%202026-27%5CB%20Voc%20-%20Program%20Document%20-%202026-27%5CProgram%20Document-B.Sc%20Animation%20and%20Visual%20Effects.pdf"

        "\n\n📞 *Contact Details*\n"
        "━━━━━━━━━━━━━━━\n"
        "📍 GM University, Davangere\n"
        "☎️ Phone: +91 9364099712,+91 9364099720\n"
        # "📧 Email: bsc.ave@gmu.ac.in\n"
    )

    payload = WhatsAppTextReplyRequest(
        to=wa_id,
        text=TextBody(
            body=text,
            preview_url=True
        ),
    )

    return payload.model_dump()


def build_bsc_ave_fee_duration_payload(wa_id: str):
    """Builds a well-formatted WhatsApp text payload for B.Sc Animation and Visual Effects fee information."""

    text = (
        "🎓 *GM University – B.Sc Animation and Visual Effects Fee Details*\n\n"

        "📌 Fee details will be updated by the university admission office.\n\n"

        "📘 *Program Information:*\n"
        "━━━━━━━━━━━━━━━\n"
        "• Creative and skill-based program\n"
        "• Animation and VFX practical training\n"
        "• Digital media and design learning\n"
        "• Studio and project-based learning\n"
        "• Career opportunities in animation, VFX and media industries\n"
        "━━━━━━━━━━━━━━━\n\n"

        "📞 *Contact Details*\n"
        "━━━━━━━━━━━━━━━\n"
        "📍 GM University, Davangere\n"
        "☎️ Phone: +91 9364099712,+91 9364099720\n"
        # "📧 Email: bsc.ave@gmu.ac.in\n"
    )

    payload = WhatsAppTextReplyRequest(
        to=wa_id,
        text=TextBody(
            body=text,
            preview_url=False
        ),
    )

    return payload.model_dump()


def build_bsc_ave_branch_website_payload(wa_id: str):
    """Builds a well-formatted WhatsApp text payload for B.Sc Animation and Visual Effects information."""

    text = (
        "🎬✨ *GM University – B.Sc Animation and Visual Effects*\n\n"

        "📌 Official website/link will be updated soon.\n\n"

        "Stay connected with GM University for updates regarding:\n"
        "━━━━━━━━━━━━━━━\n"
        "• Program Overview\n"
        "• Curriculum Details\n"
        "• Animation Studio Training\n"
        "• VFX and Editing Facilities\n"
        "• Digital Design Workshops\n"
        "• Admission Information\n"
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
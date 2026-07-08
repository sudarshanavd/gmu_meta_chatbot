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

def build_dme_program_payload(wa_id: str):
    """Builds the payload for the Digital Marketing and E-Commerce program."""

    header = MessageHeader(
        text="📱🛒 Digital Marketing & E-Commerce"
    )

    body = MessageBody(
        text=(
            "🎓 *B.Com in Digital Marketing & E-Commerce (DME)*\n\n"
            "Learn core concepts in:\n"
            "• Digital Marketing Fundamentals\n"
            "• Search Engine Optimization (SEO)\n"
            "• Social Media Marketing\n"
            "• Search Engine Marketing (SEM)\n"
            "• Content Marketing\n"
            "• E-Commerce Management\n"
            "• Web Analytics\n"
            "• Email Marketing\n"
            "• Online Consumer Behavior\n"
            "• Digital Business Strategies\n\n"
            "Get details about the program, fee structure, placements, "
            "and department information.\n\n"
            "Please choose an option below 👇"
        )
    )

    footer = MessageFooter(
        text="🎓 GM University Admissions 2026-27"
    )

    btn_program_details = Button(
        reply=ButtonReply(id="abbda", title="Program Details")
    )
    btn_fee_duration = Button(
        reply=ButtonReply(id="abbdb", title="Fee & Duration")
    )
    btn_branch_website = Button(
        reply=ButtonReply(id="abbdc", title="Branch Website")
    )

    action = ButtonAction(
        buttons=[
            btn_program_details,
            btn_fee_duration,
            btn_branch_website,
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
        interactive=interactive,
    )

    return payload.model_dump()

def build_dme_program_details_payload(wa_id: str):
    """Builds a well-formatted WhatsApp text payload for the Digital Marketing & E-Commerce program details."""

    text = (
        "🎓 *B.Com in Digital Marketing & E-Commerce (DME)*\n"
        "📘 *Program Details – 2026-27 Intake*\n\n"

        "━━━━━━━━━━━━━━━\n"
        "📄 *Program Brochure Includes:*\n"
        "• Curriculum Structure\n"
        "• Eligibility Criteria\n"
        "• Core Digital Marketing Subjects\n"
        "• E-Commerce Technologies\n"
        "• Department Highlights\n"
        "• Academic & Career Opportunities\n"
        "━━━━━━━━━━━━━━━\n\n"

       "🔗 *View Full Program Brochure:*\n"
        "Brochure will be updated soon.\n\n"

        "📞 *Contact Details*\n"
        "━━━━━━━━━━━━━━━\n"
        "📍 GM University, Davangere\n"
        "☎️ Phone: +91 9364099712,+91 9364099720\n"
        # "📧 Email: commerce@gmu.ac.in\n"
    )

    payload = WhatsAppTextReplyRequest(
        to=wa_id,
        text=TextBody(
            body=text,
            preview_url=True
        ),
    )

    return payload.model_dump()

def build_dme_fee_duration_payload(wa_id: str):
    """Builds a well-formatted WhatsApp text payload for Digital Marketing & E-Commerce fee and duration information."""

    text = (
        "🎓 *GM University – B.Com Digital Marketing & E-Commerce Fee Details*\n\n"

        "📱🛒 *Current Program Fee*\n"
        "━━━━━━━━━━━━━━━\n"
        "₹62,500 per year\n\n"

        "⏳ *Program Duration*\n"
        "━━━━━━━━━━━━━━━\n"
        "3 Years\n\n"

        "📞 *Contact Details*\n"
        "━━━━━━━━━━━━━━━\n"
        "📍 GM University, Davangere\n"
        "☎️ Phone: +91 9364099712,+91 9364099720\n"
        # "📧 Email: commerce@gmu.ac.in\n"
    )

    payload = WhatsAppTextReplyRequest(
        to=wa_id,
        text=TextBody(
            body=text,
            preview_url=True
        ),
    )

    return payload.model_dump()

def build_dme_branch_website_payload(wa_id: str):
    """Builds a well-formatted WhatsApp text payload for the Digital Marketing & E-Commerce branch website."""

    text = (
        "📱🛒 *GM University – B.Com Digital Marketing & E-Commerce*\n\n"

        "🌐 Explore the official Faculty of Commerce and Management website for:\n"
        "━━━━━━━━━━━━━━━\n"
        "• Department Overview\n"
        "• Programs Offered\n"
        "• Curriculum Structure\n"
        "• Faculty Information\n"
        "• Academic Activities\n"
        "• Placement & Career Support\n"
        "• Student Resources\n"
        "━━━━━━━━━━━━━━━\n\n"

        "🔗 *Visit Website:*\n"
        "https://faculty-of-commerce-and-management.web.app/"
    )

    payload = WhatsAppTextReplyRequest(
        to=wa_id,
        text=TextBody(
            body=text,
            preview_url=True
        ),
    )

    return payload.model_dump()
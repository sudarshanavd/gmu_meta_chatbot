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

def build_mtech_deep_learning_program_payload(wa_id: str):
    """Builds the payload for the M.Tech Deep Learning program."""

    header = MessageHeader(
        text="🤖🧠 M.Tech Deep Learning"
    )

    body = MessageBody(
        text=(
            "🎓 *M.Tech in Deep Learning*\n\n"
            "Learn core concepts in:\n"
            "• Artificial Neural Networks\n"
            "• Deep Neural Networks\n"
            "• Convolutional Neural Networks\n"
            "• Recurrent Neural Networks\n"
            "• Natural Language Processing\n"
            "• Computer Vision\n"
            "• TensorFlow & PyTorch\n"
            "• Model Training and Optimization\n"
            "• Data Engineering Basics\n"
            "• AI Model Deployment\n\n"
            "Get details about the program, eligibility, curriculum, "
            "training, practical learning, and career opportunities.\n\n"
            "Please choose an option below 👇"
        )
    )

    footer = MessageFooter(
        text="🎓 GM University Admissions 2026-27"
    )

    btn_program_details = Button(reply=ButtonReply(id="baaaa", title="Program Details"))
    btn_fee_duration = Button(reply=ButtonReply(id="baaab", title="Fee Details"))
    btn_branch_website = Button(reply=ButtonReply(id="baaac", title="More Info"))

    action = ButtonAction(buttons=[btn_program_details, btn_fee_duration, btn_branch_website])

    interactive = InteractiveButton(
        header=header,
        body=body,
        footer=footer,
        action=action,
    )

    payload = WhatsAppInteractiveButtonRequest(to=wa_id, interactive=interactive)
    return payload.model_dump()


def build_mtech_deep_learning_program_details_payload(wa_id: str):
    """Builds a well-formatted WhatsApp text payload for full M.Tech Deep Learning program details."""

    text = (
        "🎓 *M.Tech in Deep Learning*\n"
        "📘 *Program Details – 2026-27 Intake*\n\n"

        "━━━━━━━━━━━━━━━\n"
        "📄 *Program Document Includes:*\n"
        "• Curriculum Structure\n"
        "• Eligibility Criteria\n"
        "• Deep Learning Core Subjects\n"
        "• AI & Data Engineering Concepts\n"
        "• Practical & Industry-Oriented Learning\n"
        "• Academic & Career Opportunities\n"
        "━━━━━━━━━━━━━━━\n\n"

        "🔗 *View Full Program Document:*\n"
        "https://gmu.ac.in/imgview?dummy=data2024&base=assets%2Fdownloadmaterial%2FGMU%20School%20of%20Advanced%20%20Studies%20%20Pdf%20Final%2FData%20Engineering%2FData%20Engineering-&ext=png"

        "📞 *Contact Details*\n"
        "━━━━━━━━━━━━━━━\n"
        "📍 GM University, Davangere\n"
        "☎️ Phone: +91 9364099712,+91 9364099720\n"
        # "📧 Email: mtech.deeplearning@gmu.ac.in\n"
    )

    payload = WhatsAppTextReplyRequest(
        to=wa_id,
        text=TextBody(
            body=text,
            preview_url=True
        ),
    )

    return payload.model_dump()


def build_mtech_deep_learning_fee_duration_payload(wa_id: str):
    """Builds a well-formatted WhatsApp text payload for M.Tech Deep Learning fee information."""

    text = (
        "🎓 *GM University – M.Tech Deep Learning Fee Details*\n\n"

        "📌 Fee details\n"
        "━━━━━━━━━━━━━━━\n"
        "₹1,25,000\n\n"

        "⏳ *Program Duration*\n"
        "━━━━━━━━━━━━━━━\n"
        "2 Years \n\n"

        "📘 *Program Information:*\n"
        "━━━━━━━━━━━━━━━\n"
        "• Advanced AI and deep learning focused program\n"
        "• Neural network model training\n"
        "• Computer vision and NLP applications\n"
        "• Python-based practical learning\n"
        "• Career opportunities in AI, data science and research sectors\n"
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


def build_mtech_deep_learning_branch_website_payload(wa_id: str):
    """Builds a well-formatted WhatsApp text payload for M.Tech Deep Learning information."""

    text = (
        "🤖🧠 *GM University – M.Tech Deep Learning*\n\n"

        "📌 Official website/link will be updated soon.\n\n"

        "Stay connected with GM University for updates regarding:\n"
        "━━━━━━━━━━━━━━━\n"
        "• Program Overview\n"
        "• Curriculum Details\n"
        "• Practical Training\n"
        "• AI Lab Learning\n"
        "• Deep Learning Projects\n"
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
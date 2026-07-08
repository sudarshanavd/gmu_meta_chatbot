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


def build_pgd_accounting_finance_program_payload(wa_id: str):
    """Builds the payload for the PGD in Accounting and Finance with Tally program."""

    header = MessageHeader(
        text="📊💼 PGD in Accounting & Finance with Tally"
    )

    body = MessageBody(
        text=(
            "🎓 *PGD in Accounting & Finance with Tally*\n\n"
            "Learn core concepts in:\n"
            "• Financial Accounting\n"
            "• Cost Accounting\n"
            "• Management Accounting\n"
            "• Corporate Finance\n"
            "• Taxation Basics\n"
            "• GST Accounting\n"
            "• Tally Prime\n"
            "• Payroll Management\n"
            "• Financial Reporting\n"
            "• Banking and Business Transactions\n\n"
            "Get details about the program, eligibility, curriculum, "
            "industry exposure, practical learning, and career opportunities.\n\n"
            "Please choose an option below 👇"
        )
    )

    footer = MessageFooter(
        text="🎓 GM University Admissions 2026-27"
    )

    action = ButtonAction(
        buttons=[
            Button(reply=ButtonReply(id="bgaca", title="Program Details")),
            Button(reply=ButtonReply(id="bgacb", title="Fee Details")),
            Button(reply=ButtonReply(id="bgacc", title="More Info")),
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


def build_pgd_accounting_finance_program_details_payload(wa_id: str):
    """Builds a WhatsApp text payload for PGD in Accounting and Finance with Tally program details."""

    text = (
        "🎓 *PGD in Accounting & Finance with Tally*\n"
        "📘 *Program Details – 2026-27 Intake*\n\n"
        "━━━━━━━━━━━━━━━\n"
        "📄 *Program Details Include:*\n"
        "• Curriculum Structure\n"
        "• Eligibility Criteria\n"
        "• Accounting and Finance Concepts\n"
        "• Tally Prime Training\n"
        "• GST and Taxation Basics\n"
        "• Practical & Project-Based Training\n"
        "• Career Opportunities\n"
        "━━━━━━━━━━━━━━━\n\n"
        "📞 *Contact Details*\n"
        "━━━━━━━━━━━━━━━\n"
        "📍 GM University, Davangere\n"
        "☎️ Phone: +91 9364099712,+91 9364099720\n"
        # "📧 Email: info@gmu.ac.in"
    )

    payload = WhatsAppTextReplyRequest(
        to=wa_id,
        text=TextBody(
            body=text,
            preview_url=False
        ),
    )

    return payload.model_dump()


def build_pgd_accounting_finance_fee_duration_payload(wa_id: str):
    """Builds a WhatsApp text payload for PGD in Accounting and Finance with Tally fee information."""

    text = (
        "🎓 *GM University – PGD in Accounting & Finance with Tally Fee Details*\n\n"
        
        "💰 *Program Fee:* ₹55,000\n\n"
        "📘 *Program Information:*\n"
        "━━━━━━━━━━━━━━━\n"
        "• Industry-focused postgraduate diploma program\n"
        "• Strong foundation in accounting, finance, taxation, and GST\n"
        "• Hands-on learning with Tally Prime software\n"
        "• Practical training through accounts, payroll, and financial reporting\n"
        "• Career opportunities in Accounting, Finance, Taxation, Banking, Payroll, and Business Operations\n"
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


def build_pgd_accounting_finance_more_info_payload(wa_id: str):
    """Builds a WhatsApp text payload for PGD in Accounting and Finance with Tally information."""

    text = (
        "📊💼 *GM University – PGD in Accounting & Finance with Tally*\n\n"
        "Learn practical concepts and industry applications in:\n\n"
        "━━━━━━━━━━━━━━━\n"
        "• Accounting Principles\n"
        "• Financial Management\n"
        "• Tally Prime\n"
        "• GST Accounting\n"
        "• Taxation Basics\n"
        "• Payroll Management\n"
        "• Financial Reporting\n"
        "• Business Transactions\n"
        "━━━━━━━━━━━━━━━\n\n"
        "Enhance your skills with practical accounting and finance-based learning."
    )

    payload = WhatsAppTextReplyRequest(
        to=wa_id,
        text=TextBody(
            body=text,
            preview_url=False
        ),
    )

    return payload.model_dump()
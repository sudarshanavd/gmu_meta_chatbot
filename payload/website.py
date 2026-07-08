def build_website_payload(wa_id: str):
    payload = {
        "messaging_product": "whatsapp",
        "recipient_type": "individual",
        "to": wa_id,
        "type": "interactive",
        "interactive": {
            "type": "cta_url",
            "header": {
                "type": "text",
                "text": "🎓 GM University Admissions 2026-27"
            },
            "body": {
                "text": (
                    "Welcome to *GM University Admissions Helpdesk* 👋\n\n"
                    "Click the button below to visit our official website."
                )
            },
            "footer": {
                "text": "📍 GM University | Empowering Future Innovators"
            },
            "action": {
                "name": "cta_url",
                "parameters": {
                    "display_text": "🌐 Visit Website",
                    "url": "https://gmu.ac.in/"
                }
            }
        }
    }

    return payload
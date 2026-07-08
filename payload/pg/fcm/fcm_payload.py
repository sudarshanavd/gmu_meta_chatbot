from schema.service_schema import (WhatsAppInteractiveButtonRequest, 
								   InteractiveButton, 
								   MessageBody, MessageHeader, 
								   MessageFooter, ButtonAction,
								   Button,ButtonReply,
								   WhatsAppInteractiveListRequest,
								   ListSection, ListRow, ListAction,InteractiveList,
								   WhatsAppTextReplyRequest, TextBody
)


def build_pg_fcm_payload(wa_id: str):
	"""Builds the payload for PG Faculty of Commerce & Management."""

	header = MessageHeader(
		text="🏫 Faculty of Commerce & Management"
	)

	body = MessageBody(
		text=(
			"Welcome to the *PG Faculty of Commerce & Management* 👋\n\n"
			"Explore postgraduate programs in commerce, finance, and management.\n\n"
			"Please choose a school to view available programs 👇"
		)
	)

	footer = MessageFooter(
		text="🎓 GM University Admissions 2026-27"
	)

	btn_school_commerce = Button(reply=ButtonReply(id="bda", title="School of Commerce"))
	btn_gmbs = Button(reply=ButtonReply(id="bdb", title="GM Business School"))

	action = ButtonAction(buttons=[btn_school_commerce, btn_gmbs])

	interactive = InteractiveButton(
		header=header,
		body=body,
		footer=footer,
		action=action,
	)

	payload = WhatsAppInteractiveButtonRequest(to=wa_id, interactive=interactive)
	return payload.model_dump()


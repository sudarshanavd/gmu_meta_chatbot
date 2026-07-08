from schema.service_schema import (WhatsAppInteractiveButtonRequest, 
								   InteractiveButton, 
								   MessageBody, MessageHeader, 
								   MessageFooter, ButtonAction,
								   Button,ButtonReply,
								   WhatsAppInteractiveListRequest,
								   ListSection, ListRow, ListAction,InteractiveList,
								   WhatsAppTextReplyRequest, TextBody
)


def build_pg_school_of_commerce_payload(wa_id: str):
	"""Builds the payload for PG School of Commerce programs."""

	header = MessageHeader(
		text="💼 School of Commerce"
	)

	body = MessageBody(
		text=(
			"Welcome to the *PG School of Commerce* 👋\n\n"
			"Explore M.Com and related postgraduate programs in finance, digital business,\n"
			"and fintech analytics.\n\n"
			"Please choose a program below 👇"
		)
	)

	footer = MessageFooter(
		text="🎓 GM University Admissions 2026-27"
	)

	sections = [
		ListSection(
			title="M.Com Programs",
			rows=[
				ListRow(
					id="bdaa",
					title="M.Com - Applied Finance & Digital Business",
					description="Applied Finance and Digital Business"
				),
				ListRow(
					id="bdab",
					title="Fintech Analytics & Entrepreneurship",
					description="Fintech Analytics and Entrepreneurship"
				)
			]
		)
	]

	action = ListAction(button="Choose Program", sections=sections)

	interactive = InteractiveList(
		header=header,
		body=body,
		footer=footer,
		action=action,
	)

	payload = WhatsAppInteractiveListRequest(to=wa_id, interactive=interactive)
	return payload.model_dump()


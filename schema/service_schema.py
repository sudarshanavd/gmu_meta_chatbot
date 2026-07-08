from pydantic import BaseModel, Field
from typing import List, Optional

# ─── Interactive button message models ─────────
class ButtonReply(BaseModel):
    id: str
    title: str = Field(..., min_length=1, max_length=20)


class Button(BaseModel):
    type: str = "reply"
    reply: ButtonReply


class ButtonAction(BaseModel):
    buttons: List[Button] = Field(default_factory=list, max_items=3)


class MessageBody(BaseModel):
    text: str


class MessageHeader(BaseModel):
    type: str = "text"
    text: Optional[str] = None


class MessageFooter(BaseModel):
    text: str


class InteractiveButton(BaseModel):
    type: str = "button"
    header: Optional[MessageHeader] = None
    body: MessageBody
    footer: Optional[MessageFooter] = None
    action: ButtonAction


class WhatsAppInteractiveButtonRequest(BaseModel):
    messaging_product: str = "whatsapp"
    recipient_type: str = "individual"
    to: str
    type: str = "interactive"
    interactive: InteractiveButton

# ─── Interactive list message models ─────────

class ListRow(BaseModel):
    id: str
    title: str = Field(..., max_length=24)
    description: Optional[str] = None


class ListSection(BaseModel):
    title: str
    rows: List[ListRow] = Field(default_factory=list)


class ListAction(BaseModel):
    button: str
    sections: List[ListSection] = Field(default_factory=list)


class InteractiveList(BaseModel):
    type: str = "list"
    header: Optional[MessageHeader] = None
    body: MessageBody
    footer: Optional[MessageFooter] = None
    action: ListAction


class WhatsAppInteractiveListRequest(BaseModel):
    messaging_product: str = "whatsapp"
    recipient_type: str = "individual"
    to: str
    type: str = "interactive"
    interactive: InteractiveList


# ─── Text message with optional reply context ─────────

class ReplyContext(BaseModel):
    message_id: str


class TextBody(BaseModel):
    body: str
    preview_url: Optional[bool] = False


class WhatsAppTextReplyRequest(BaseModel):
    """Text message payload with optional context for replying to a specific message."""
    messaging_product: str = "whatsapp"
    recipient_type: str = "individual"
    to: str
    type: str = "text"
    text: TextBody
    context: Optional[ReplyContext] = None


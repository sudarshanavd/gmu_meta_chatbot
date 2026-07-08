from pydantic import BaseModel, Field


# ─── Blue tick (mark as read) ──────────────────────────

class MarkAsRead(BaseModel):
    """Payload to mark a message as read (blue tick)."""
    messaging_product: str = "whatsapp"
    status: str = "read"
    message_id: str


# ─── Typing indicator ─────────────────────────────────

class TypingIndicatorType(BaseModel):
    type: str = "text"


class MarkAsReadWithTyping(BaseModel):
    """Payload to mark as read AND show typing indicator."""
    messaging_product: str = "whatsapp"
    status: str = "read"
    message_id: str
    typing_indicator: TypingIndicatorType = Field(default_factory=TypingIndicatorType)


# ─── Reaction emoji ───────────────────────────────────

class Reaction(BaseModel):
    """Reaction sub-object."""
    message_id: str
    emoji: str


class ReactionMessage(BaseModel):
    """Payload to send a reaction emoji on a message."""
    messaging_product: str = "whatsapp"
    recipient_type: str = "individual"
    to: str
    type: str = "reaction"
    reaction: Reaction


# ─── Reply to message ─────────────────────────────────

class ReplyContext(BaseModel):
    """Context sub-object to reference the message being replied to."""
    message_id: str


class ReplyMessage(BaseModel):
    """Payload to send a message as a reply to a specific message."""
    messaging_product: str = "whatsapp"
    recipient_type: str = "individual"
    to: str
    context: ReplyContext

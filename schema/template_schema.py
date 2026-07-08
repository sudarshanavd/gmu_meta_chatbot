from pydantic import BaseModel, Field
from typing import List, Dict, Any, Optional


class Action(BaseModel):
    flow_token: Optional[str] = "unused"
    flow_action_data: Optional[Dict[str, Any]] = None


class Parameter(BaseModel):
    type: str
    action: Optional[Action] = None


class Component(BaseModel):
    type: str
    sub_type: Optional[str] = None
    index: Optional[str] = None
    parameters: List[Parameter] = Field(default_factory=list)


class Language(BaseModel):
    code: str


class Template(BaseModel):
    name: str
    language: Language
    components: List[Component] = Field(default_factory=list)


class WhatsAppTemplateRequest(BaseModel):
    messaging_product: str = "whatsapp"
    recipient_type: str = "individual"
    to: str
    type: str = "template"
    template: Template
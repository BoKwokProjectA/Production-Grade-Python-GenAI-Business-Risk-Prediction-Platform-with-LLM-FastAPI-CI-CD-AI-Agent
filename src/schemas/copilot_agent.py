"""
Schemas used by the Copilot Studio support-agent endpoint.
"""

from pydantic import BaseModel, Field


class CopilotSupportRequest(BaseModel):
    question: str = Field(..., min_length=3, max_length=1000)
    conversation_id: str | None = None
    user_role: str | None = "user"


class CopilotSupportResponse(BaseModel):
    answer: str
    intent: str
    risk_level: str
    automation_allowed: bool
    escalation_required: bool
    sources: list[str]
    safety_note: str

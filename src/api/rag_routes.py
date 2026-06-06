"""
Routes of RAG Assistant
"""

from fastapi import APIRouter
from pydantic import BaseModel

from src.rag.rag_engine import RAGEngine

rag_router = APIRouter()
rag_engine = RAGEngine()


class ChatRequest(BaseModel):
    question: str


class ChatResponse(BaseModel):
    answer: str


@rag_router.post("/chat", response_model=ChatResponse)
async def chat_with_assistant(request: ChatRequest):
    """Chat with the RAG assistant"""
    answer = rag_engine.ask(request.question)
    return ChatResponse(answer=answer)

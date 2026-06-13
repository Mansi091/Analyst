from fastapi import APIRouter
from pydantic import BaseModel

from agents.analyst_agent import data_analyst_agent


router = APIRouter(
    prefix="/agent",
    tags=["Data Analyst Agent"]
)


class AgentRequest(BaseModel):
    filename: str
    question: str


@router.post("/ask")
def ask_agent(request: AgentRequest):

    user_message = f"""
Filename: {request.filename}

User question:
{request.question}
"""

    response = data_analyst_agent.invoke({
        "messages": [
            {"role": "user", "content": user_message}
        ]
    })

    answer = response["messages"][-1].content

    return {
        "answer": answer
    }
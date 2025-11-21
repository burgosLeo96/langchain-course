from typing import List

from pydantic import BaseModel, Field
from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain_core.messages import HumanMessage
from langchain_openai.chat_models import ChatOpenAI
from langchain_tavily import TavilySearch

load_dotenv()

class Source(BaseModel):
    """Schema for a source used by the agent."""

    url:str = Field(description="The URL of the source.")


class AgentResponse(BaseModel):
    """Schema for the agent's response."""

    answer: str = Field(description="The final answer provided by the agent.")
    sources: List[Source] = Field(default_factory=List, description="List of sources used to generate the answer.")


llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)
tools = [TavilySearch()]
agent = create_agent(model=llm, tools=tools, response_format=AgentResponse)

def main():
    print("Hello from langchain-course!")
    result = agent.invoke({"messages":HumanMessage(content="What's the weather like in Tokyo?")})
    print(result)


if __name__ == "__main__":
    main()

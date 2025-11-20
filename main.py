from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_openai.chat_models import ChatOpenAI
from tavily import TavilyClient

load_dotenv()

tavily = TavilyClient()

@tool
def search(query: str) -> str:
    """Tool that searches on the internet.
        Args:
            query (str): The search query.
        Returns:
            str: The search results.
    """

    print(f"Searching for: {query}")
    return tavily.search(query=query)

llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)
tools = [search]
agent = create_agent(model=llm, tools=tools)

def main():
    print("Hello from langchain-course!")
    result = agent.invoke({"messages":HumanMessage(content="What's the weather like in Tokyo?")})
    print(result)


if __name__ == "__main__":
    main()

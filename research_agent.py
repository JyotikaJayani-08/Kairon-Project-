from langchain.agents import AgentExecutor, create_tool_calling_agent
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from utils.tools import get_tavily_tool
from langchain_groq import ChatGroq  
import os

# from langchain_openai import ChatOpenAI
from utils.tools import get_tavily_tool


# from langchain_community.chat_models import ChatGroq  # If using LangChain's Groq integration
# self.llm = ChatGroq(model="mixtral-8x7b-32768", temperature=0.7)


class ResearchAgent:
    def __init__(self):
        
        self.llm = ChatGroq(model="llama-3.3-70b-versatile", temperature=0,groq_api_key=os.getenv("GROQ_API_KEY"))
        self.tools = [get_tavily_tool()]
        self.prompt = ChatPromptTemplate.from_messages([
            ("system", """You are a world-class researcher. Conduct thorough research on any topic.
            Use Tavily to search for high-quality information.
            Provide detailed summaries with sources."""),
            ("user", "{input}"),
            MessagesPlaceholder(variable_name="agent_scratchpad")
        ])
        self.agent = create_tool_calling_agent(self.llm, self.tools, self.prompt)
        self.agent_executor = AgentExecutor(
            agent=self.agent, 
            tools=self.tools, 
            verbose=True,
            handle_parsing_errors=True
        )

    def research(self, query: str) -> str:
        result = self.agent_executor.invoke({"input": query})
        return result["output"]
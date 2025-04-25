from langchain.agents import AgentExecutor, create_tool_calling_agent
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_groq import ChatGroq
import os


# from langchain_openai import ChatOpenAI
# from langchain_community.chat_models import ChatGroq  # If using LangChain's Groq integration
# self.llm = ChatGroq(model="mixtral-8x7b-32768", temperature=0.7)



class DraftingAgent:
    def __init__(self):
        
        self.llm = ChatGroq(model="llama-3.3-70b-versatile", temperature=0.7,groq_api_key=os.getenv("GROQ_API_KEY"))
        self.prompt = ChatPromptTemplate.from_messages([
            ("system", """You are an expert content writer. Synthesize research into:
            1. Well-structured answers
            2. Clear explanations
            3. Proper citations
            4. Multiple perspectives"""),
            ("user", "{input}"),
            MessagesPlaceholder(variable_name="agent_scratchpad")
        ])
        self.agent = create_tool_calling_agent(self.llm, [], self.prompt)
        self.agent_executor = AgentExecutor(
            agent=self.agent, 
            tools=[], 
            verbose=True,
            handle_parsing_errors=True
        )

    def draft_response(self, research_data: str) -> str:
        result = self.agent_executor.invoke({
            "input": f"Based on this research data, draft a comprehensive answer:\n\n{research_data}"
        })
        return result["output"]
    
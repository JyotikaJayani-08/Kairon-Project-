from typing import Dict, List, Union, Tuple, Type
from langchain_core.messages import BaseMessage, HumanMessage, AIMessage
from langchain_core.prompts.chat import BaseMessagePromptTemplate, BaseChatPromptTemplate
from langgraph.graph import END, MessageGraph
from agents.research_agent import ResearchAgent
from agents.drafting_agent import DraftingAgent

MessageLikeRepresentation = Union[
    Union[BaseMessagePromptTemplate, BaseMessage, BaseChatPromptTemplate],
    Tuple[Union[str, Type], Union[str, List[Dict], List[object]]],
    str
]

def convert_to_message(representation: MessageLikeRepresentation) -> BaseMessage:
    """Universal message converter (now defined at module level)"""
    if isinstance(representation, BaseMessage):
        return representation
    elif isinstance(representation, str):
        return HumanMessage(content=representation)
    elif isinstance(representation, tuple):
        role, content = representation
        if isinstance(role, type) and issubclass(role, BaseMessage):
            return role(content=content)
        return HumanMessage(content=str(content), additional_kwargs={"role": str(role)})
    return HumanMessage(content=str(representation))

def create_research_workflow():
    research_agent = ResearchAgent()
    drafting_agent = DraftingAgent()
    
    workflow = MessageGraph()
    
    def research_node(state: Dict[str, List[BaseMessage]]) -> Dict[str, List[BaseMessage]]:
        last_message = state["messages"][-1]
        research_result = research_agent.research(last_message.content)
        return {"messages": [AIMessage(content=research_result)]}

    def draft_node(state: Dict[str, List[BaseMessage]]) -> Dict[str, List[BaseMessage]]:
        last_message = state["messages"][-1]
        draft_result = drafting_agent.draft_response(last_message.content)
        return {"messages": [AIMessage(content=draft_result)]}

    workflow.add_node("research", research_node)
    workflow.add_node("draft", draft_node)
    
    workflow.add_edge("research", "draft")
    workflow.add_edge("draft", END)
    
    workflow.set_entry_point("research")
    
    return workflow.compile()

def run_research_workflow(query: MessageLikeRepresentation) -> str:
    workflow = create_research_workflow()
    
    # Use the module-level converter
    initial_message = convert_to_message(query)
    
    result = workflow.invoke({
        "messages": [initial_message]
    })
    
    return result["messages"][-1].content



# # Test all input formats
# test_cases = [
#     "plain string query",
#     ("user", "tuple formatted query"),
#     HumanMessage(content="direct message"),
#     ["will", "be", "stringified"],
#     {"complex": "object"}
# ]

# for query in test_cases:
#     try:
#         print(f"\nInput: {query}")
#         print("Result:", run_research_workflow(query)[:100] + "...")
#     except Exception as e:
#         print(f"Error: {type(e).__name__}: {str(e)}")
from langchain_community.tools.tavily_search import TavilySearchResults
from dotenv import load_dotenv
import os

load_dotenv()

def get_tavily_tool():
    return TavilySearchResults(
        api_key=os.getenv("TAVILY_API_KEY"),
        search_depth="advanced",
        include_raw_content=True,
        include_images=True,
        max_results=5
    )
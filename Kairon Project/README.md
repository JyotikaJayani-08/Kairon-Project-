
# KAIRON: Deep Research AI Agentic System

## Overview
KAIRON is a dual-agent AI system powered by LangChain and LangGraph, designed to perform deep web-based research using the Tavily API. It includes:
- A **Research Agent** to gather online content.
- An **Answer Agent** to draft intelligent, contextual answers.



# Research Agent System 🤖🔍

A LangChain-powered AI research assistant that automates:
- Web research using Tavily
- Content synthesis
- Multi-perspective analysis
- Proper citation generation

## Features ✨

- **Two-Stage Workflow**:
  - 🕵️ Research Agent: Conducts deep web searches
  - ✍️ Drafting Agent: Creates polished outputs
- **Flexible Input Handling**:
  - Accepts strings, tuples, or LangChain message objects
- **Production-Ready**:
  - Error handling
  - Type annotations
  - Environment variable configuration

## Installation ⚙️

# Clone repository
git clone https://github.com/JyotikaJayani-08/Kairon-Project.git
cd research-agent

# Install dependencies
pip install -r requirements.txt

# Set up API keys in .env file
echo "TAVILY_API_KEY=your_key_here" >> .env
echo "GROQ_API_KEY=your_key_here" >> .env  # or GOOGLE_API_KEY for Gemini


## Usage 🚀

### Basic Usage

from main import main
main()  # Interactive CLI mode


### Programmatic Usage

from graphs.research_graph import run_research_workflow

result = run_research_workflow(
    "Explain quantum computing applications in medicine"
)
print(result)



### System Architecture
![deepseek_mermaid_20250425_67f7e1](https://github.com/user-attachments/assets/8b572ece-c5fb-4906-b90f-7749ea73479c)



### Supported Input Formats

# As string
run_research_workflow("Simple query")

# As tuple (role, content)
run_research_workflow(("user", "Tuple formatted query"))

# As LangChain message
from langchain_core.messages import HumanMessage
run_research_workflow(HumanMessage(content="Structured message"))


## Project Structure 🗂️

research_agent/
├── agents/               # Agent implementations
│   ├── research_agent.py # Web research specialist
│   └── drafting_agent.py # Content synthesis expert
├── graphs/               # Workflow orchestration
│   └── research_graph.py # Research→Draft pipeline
├── utils/                # Tools and utilities
│   └── tools.py          # Tavily search wrapper
├── main.py               # CLI interface
└── .env                  # API keys


## Configuration ⚙️
| Variable          | Description                     | Required |
|-------------------|---------------------------------|----------|
| `TAVILY_API_KEY`  | Tavily search API key           | Yes      |
| `GROQ_API_KEY`    | Groq API key (or Google/Gemini) | Yes      |

## Customization 🛠️

### Switching LLM Providers
Edit `agents/research_agent.py`:

# For Gemini:
from langchain_google_genai import ChatGoogleGenerativeAI
self.llm = ChatGoogleGenerativeAI(model="gemini-pro")

# For Groq:
from langchain_groq import ChatGroq
self.llm = ChatGroq(model="llama-3.3-70b-versatile")


### Adding New Tools
1. Add to `utils/tools.py`:

from langchain.tools import Tool

def get_new_tool():
    return Tool(
        name="New Tool",
        func=lambda x: "Results",
        description="Tool description"
    )

2. Update ResearchAgent:

from utils.tools import get_new_tool
self.tools = [get_tavily_tool(), get_new_tool()]


## Troubleshooting 🐛

| Error | Solution |
|-------|----------|
| Message format errors | Ensure inputs are strings, tuples, or BaseMessage |
| API connection issues | Verify .env file exists with valid keys |
| ModuleNotFoundError | Run `pip install -r requirements.txt` |



### Output 
![output ](https://github.com/user-attachments/assets/7f27735e-bc1c-4665-af72-1d6a57bcd100)



## Roadmap 🗺️
- [ ] Add PDF/arXiv research capabilities
- [ ] Implement auto-citation formatting
- [ ] Add multi-language support
- [ ] Build web interface

## License 📄
MIT License - Free for academic and commercial use


Key documentation features included:
1. **Visual hierarchy** with emojis and clear sections
2. **Multiple usage examples** covering different scenarios
3. **Configuration table** for environment variables
4. **Customization guide** for extending functionality
5. **Troubleshooting section** for common issues
6. **Future roadmap** for project evolution


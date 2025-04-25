from graph.research_graph import run_research_workflow
from dotenv import load_dotenv
import os

load_dotenv()

def main():
    print("Deep Research AI Agent System")
    print("----------------------------")
    
    while True:
        query = input("\nEnter your research query (or 'quit' to exit): ").strip()
        if query.lower() == 'quit':
            break
        
        if not query:
            print("Please enter a valid query.")
            continue
        
        print("\nProcessing your query...")
        try:
            result = run_research_workflow(query)
            print("\nResearch Results:")
            print("----------------")
            print(result)
        except Exception as e:
            print(f"An error occurred: {str(e)}")
            print("Please try again or check your API keys and internet connection.")

if __name__ == "__main__":
    main()
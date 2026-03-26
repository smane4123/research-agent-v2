from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.agents import initialize_agent

from tools.csv_tool import csv_tool
from tools.web_tool import web_tool

# Load environment variables
load_dotenv()

# LLM (OpenRouter working model)
llm = ChatOpenAI(
    model="openai/gpt-3.5-turbo",
    temperature=0
)

tools = [csv_tool, web_tool]

agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent="zero-shot-react-description",
    verbose=True,
    agent_kwargs={
        "system_message": """
You are a Research Assistant Agent.

Your job:
1. Analyze CSV data using CSV tool
2. Use Web Search for latest trends
3. Combine both insights
4. Give clear structured answer

Always:
- Extract insights (not raw data)
- Compare dataset with real-world trends
- Provide meaningful conclusions
"""
    }
)
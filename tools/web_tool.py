from dotenv import load_dotenv
from langchain.tools import Tool
from langchain_community.tools.tavily_search import TavilySearchResults

load_dotenv()

tavily = TavilySearchResults()

def formatted_web_search(query):
    results = tavily.run(query)

    if isinstance(results, str):
        return results

    output = "\n🌐 Key Web Insights:\n"

    try:
        for i, res in enumerate(results[:3], start=1):
            output += f"""
🔎 Result {i}
Title   : {res.get('title', '')}
Summary : {res.get('content', '')[:150]}...
Source  : {res.get('url', '')}
"""
    except:
        return str(results)

    return output


web_tool = Tool(
    name="Web Search",
    func=formatted_web_search,
    description="Use this tool to get latest real-world trends and insights"
)
from agent.agent_setup import agent

def run_agent(query: str):
    try:
        response = agent.invoke({"input": query})

        if isinstance(response, dict) and "output" in response:
            return response["output"]
        else:
            return str(response)

    except Exception as e:
        return f"❌ Error: {str(e)}"
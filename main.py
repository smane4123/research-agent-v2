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


# OPTIONAL: Keep CLI mode (safe)
if __name__ == "__main__":
    print("🤖 Research Agent Ready! (type 'exit' to quit)\n")

    while True:
        query = input("Enter your query: ")

        if query.lower() == "exit":
            break

        result = run_agent(query)
        print("\n✅ Final Answer:\n", result)
        print("\n" + "-"*50 + "\n")

        

        
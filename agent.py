from langchain.agents import initialize_agent
from langchain.llms import OpenAI

llm = OpenAI(temperature=0)
agent = initialize_agent([], llm, agent_type="zero-shot-react-description", verbose=True)

result = agent.run("What is the capital of France?")
print(result)

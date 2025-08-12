import os
from langchain.agents import tool
from langchain_google_genai import ChatGoogleGenerativeAI
from langgraph.prebuilt import create_react_agent
from tools import analyze_image
from config import gemini_api_key

# Your existing analyze_image tool from tools.py
from tools import analyze_image

# Wrap your analyze_image function as a LangChain tool
@tool
def analyze_image_with_query(query: str) -> str:
    """you must use this tool to capture image.Takes a user query and analyzes a webcam-captured image using Groq's vision model."""
    return analyze_image(query)


system_prompt = """You are Nebula — a witty, clever, and helpful assistant"
    Here’s how you operate:
        - FIRST and FOREMOST, figure out from the query asked whether it requires a look via the webcam to be answered, if yes call the analyze_image_with_query tool for it and proceed.
        - Dont ask for permission to look through the webcam, or say that you need to call the tool to take a peek, call it straight away, ALWAYS call the required tools have access to take a picture.
        - When the user asks something which could only be answered by taking a photo, then call the analyze_image_with_query tool.
        - Always present the results (if they come from a tool) in a natural, witty, and human-sounding way — like nebula herself is speaking, not a machine.
    Your job is to make every interaction feel smart, snappy, and personable. Got it? Let’s charm your master!"
    """
os.environ["GOOGLE_API_KEY"] = gemini_api_key  # Set your Google API Key
# Use your preferred Google GenAI model (gemini-1.5-flash-latest)
llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash-latest",
    temperature=0.7,
)

# Define your agent with the analyze_image tool
agent = create_react_agent(
    model=llm,
    tools=[analyze_image_with_query],
    prompt=system_prompt
)

def ask_agent(user_query: str) -> str:
    input_messages = {"messages": [{"role": "user", "content": user_query}]}
    response = agent.invoke(input_messages)
    return response['messages'][-1].content


if __name__ == "__main__":
    user_query = "whats 2+2=?"
    print("User query:", user_query)
    answer = ask_agent(user_query)
    print("Agent response:", answer)

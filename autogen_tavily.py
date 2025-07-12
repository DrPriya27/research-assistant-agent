from autogen import register_function, ConversableAgent
from dotenv import load_dotenv
from core.tavily_search import tavily_search
from core.llm_config import llm_config

# Load environment variables
load_dotenv()


# Create an assistant agent that can use the Tavily search tool
assistant = ConversableAgent(
    name="Assistant",
    system_message="You are a helpful AI assistant with access to internet search capabilities.",
    llm_config=llm_config,
)

# Create a user proxy agent that can execute the Tavily search tool
user_proxy = ConversableAgent(name="User", human_input_mode="NEVER", llm_config=False)

# Register the Tavily search function with both agents
register_function(
    tavily_search,
    caller=assistant,
    executor=user_proxy,
    name="tavily_search",
    description="A tool to search the internet using the Tavily API",
)


def main():
    while True:
        user_input = input("User: ")

        if user_input.lower() in ["exit", "quit", "bye"]:
            print("Chatbot: Goodbye! Have a great day!")
            break

        # Initiate a chat between the user proxy and the assistant
        chat_result = user_proxy.initiate_chat(
            assistant,
            message=user_input,
            max_turns=2,
        )

        # Extract the assistant's reply from the chat history
        reply = next(
            (
                msg["content"]
                for msg in chat_result.chat_history
                if msg.get("name") == "Assistant"
            ),
            "I apologize, but I couldn't generate a response.",
        )

        print(f"Chatbot: {reply}")


if __name__ == "__main__":
    main()

    

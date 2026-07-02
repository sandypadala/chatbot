
from backend.chatbot import generate_response, get_llm, build_conversation, build_chain


def run_cli():
    print("=" * 50)
    print("Simple LangChain Chatbot (type 'exit' to quit)")
    print("=" * 50)

    llm = get_llm()

    while True:
        user_input = input("\nYou: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Goodbye!")
            break
        reply = generate_response(user_input, llm=llm)
        print(f"\nAssistant: {reply}")


if __name__ == "__main__":
    run_cli()

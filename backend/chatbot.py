from pathlib import Path
import os
from dotenv import load_dotenv

env_path = Path(__file__).resolve().parents[1] / ".env"
load_dotenv(dotenv_path=env_path)


def get_api_key():
    api_key = os.getenv("OPENAI_API_KEY")
    if api_key:
        return api_key
    raise RuntimeError("OPENAI_API_KEY environment variable is not set.")


def get_llm():
    try:
        from langchain_openai import ChatOpenAI
    except Exception as exc:
        raise RuntimeError("LangChain/OpenAI dependencies are missing or incompatible.") from exc

    return ChatOpenAI(
        model="gpt-4o-mini",
        api_key=get_api_key(),
        temperature=0.7,
    )


def build_conversation():
    try:
        from langchain_core.prompts import ChatPromptTemplate
    except Exception as exc:
        raise RuntimeError("LangChain prompt dependencies are missing or incompatible.") from exc

    return ChatPromptTemplate.from_messages(
        [
            (
                "system",
                "You are a helpful AI assistant. Answer clearly and concisely.",
            ),
            ("human", "{user_input}"),
        ]
    )


def build_chain(llm=None):
    if llm is None:
        llm = get_llm()

    try:
        from langchain_core.output_parsers import StrOutputParser
    except Exception as exc:
        raise RuntimeError("LangChain output parser dependencies are missing or incompatible.") from exc

    prompt_template = build_conversation()
    return prompt_template | llm | StrOutputParser()


def generate_response(user_input, llm=None):
    chain = build_chain(llm=llm)
    return chain.invoke({"user_input": user_input})

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import SystemMessage, HumanMessage

load_dotenv()


class DummyLLM:
    def invoke(self, prompt):
        # Simulated stateless behavior
        return f"LLM response to: '{prompt}'"


def main():
    llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", seed=6)

    print("=== ❌ Naïve Invocation (Context Break) ===")

    # First call: provides context
    resp1 = llm.invoke(
        "We are building an AI system for processing medical insurance claims."
    )

    # Second call: asks a follow-up question WITHOUT passing prior context
    resp2 = llm.invoke(
        "What are the main risks in this system?"
    )

    print("\nResponse 1:")
    print(resp1)

    print("\nResponse 2:")
    print(resp2)

    print("\n\n=== ✅ Fixed Using Messages API (Context Preserved) ===")

    # Context-aware invocation using structured messages
    messages = [
        SystemMessage(content="You are a senior AI architect reviewing production systems."),
        HumanMessage(content="We are building an AI system for processing medical insurance claims."),
        HumanMessage(content="What are the main risks in this system?")
    ]

    resp3 = llm.invoke(messages)

    print("\nResponse with context:")
    print(resp3)


if __name__ == "__main__":
    main()


# ⚠️ IMPORTANT EXPLANATION:
# The second question in the naïve approach may fail or behave inconsistently because most LLMs are stateless.
# Each `invoke` call is independent and does not retain memory of previous interactions unless explicitly provided.
#
# The follow-up question ("What are the main risks in this system?") depends on prior context,
# but since that context is not passed, the model:
#   - May not understand what "this system" refers to
#   - May return generic or unrelated risks
#   - Can produce inconsistent outputs across runs
#
# ✅ FIX:
# By passing structured messages (SystemMessage + HumanMessage),
# we provide full conversation history, enabling the LLM to:
#   - Understand context correctly
#   - Give coherent, relevant answers
#   - Behave consistently


"""
Reflection:

1. Why did string-based invocation fail?
String-based invocation failed because each LLM call is stateless and independent.
The second query relied on prior context ("this system"), but that context was not passed,
so the model lacked the necessary information to interpret the question correctly.

2. Why does message-based invocation work?
Message-based invocation works because it explicitly includes the full conversation history
(SystemMessage + HumanMessage). This allows the LLM to understand context, maintain continuity,
and generate accurate, relevant responses.

3. What would break in a production AI system if we ignore message history?
If message history is ignored in production:
- Conversations become inconsistent and confusing
- Follow-up queries lose meaning
- AI agents fail at multi-step reasoning
- User experience degrades significantly
- Critical decisions (e.g., healthcare, finance) may become incorrect due to missing context
"""
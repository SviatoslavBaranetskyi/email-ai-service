from typing import TypedDict
from langchain_ollama import OllamaLLM
from langgraph.graph import StateGraph, END
from app.domain.enums import EmailClassification
from app.ai.prompts import CLASSIFICATION_PROMPT, SUMMARY_PROMPT

class EmailState(TypedDict, total=False):
    subject: str
    body: str
    classification: str
    summary: str

class EmailAI:
    def __init__(self):
        self.llm = OllamaLLM(model="llama2")
        self.workflow = self._build_graph()

    def _build_graph(self):
        builder = StateGraph(EmailState)

        async def classify_node(state: EmailState):
            prompt = CLASSIFICATION_PROMPT.format(subject=state["subject"], body=state["body"])
            response = await self.llm.agenerate(prompt)
            return {"classification": response.text.strip().upper()}

        async def summarize_node(state: EmailState):
            prompt = SUMMARY_PROMPT.format(subject=state["subject"], body=state["body"])
            response = await self.llm.agenerate(prompt)
            return {"summary": response.text.strip()}

        builder.add_node("classifier", classify_node)
        builder.add_node("summarizer", summarize_node)

        builder.set_entry_point("classifier")
        builder.add_edge("classifier", "summarizer")
        builder.add_edge("summarizer", END)

        return builder.compile()

    async def process_email(self, subject: str, body: str):
        initial_state = {"subject": subject, "body": body}
        result = await self.workflow.ainvoke(initial_state)

        raw_class = result.get("classification", "").upper()
        classification = EmailClassification.OTHER
        if "INVOICE" in raw_class:
            classification = EmailClassification.INVOICE
        elif "MEETING" in raw_class:
            classification = EmailClassification.MEETING

        summary = result.get("summary", "")
        return classification, summary
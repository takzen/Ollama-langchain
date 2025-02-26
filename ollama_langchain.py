from langchain_ollama import OllamaLLM
from langchain.prompts import PromptTemplate

ollama_llm = OllamaLLM(model="ollama3.2")  # Model Ollama 3.2

prompt_template = """
Odpowiedz na pytanie: {question}
"""
prompt = PromptTemplate(template=prompt_template, input_variables=["question"])

chain = prompt | ollama_llm

question = "Jaka jest stolica Polski?"
response = chain.invoke({"question": question})

print(f"Pytanie: {question}")
print(f"Odpowiedź: {response.text if hasattr(response, 'text') else response}")
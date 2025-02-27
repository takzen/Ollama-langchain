'''4. Ulepszenie szablonu promptu.
   Możesz zmodyfikować prompt_template, żeby odpowiedzi 
   były bardziej precyzyjne lub miały określony styl, np.: 
   Dlaczego? Dodanie instrukcji w szablonie (np. "zwięzły i 
   praktyczny") może wpłynąć na styl odpowiedzi modelu, co 
   jest przydatne, jeśli chcesz konkretnych rezultatów.'''

from langchain_ollama import OllamaLLM
from langchain.prompts import PromptTemplate

ollama_llm = OllamaLLM(
    model="llama3.2",
    endpoint="http://127.0.0.1:11434/"
)

prompt_template = """
Odpowiedz na pytanie w sposób zwięzły i praktyczny: {question}
"""
prompt = PromptTemplate(template=prompt_template, input_variables=["question"])
chain = prompt | ollama_llm

question = "Podaj przepis na rosół"
response = chain.invoke({"question": question})

print(f"Pytanie: {question}")
print(f"Odpowiedź: {response.text if hasattr(response, 'text') else response}")


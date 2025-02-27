'''6. Zapis odpowiedzi do pliku.
    Jeśli chcesz zachować odpowiedzi, możesz je zapisać do pliku.
    Dlaczego? Zapis do pliku pozwala archiwizować odpowiedzi, 
    np. do późniejszego wykorzystania.'''

from langchain_ollama import OllamaLLM
from langchain.prompts import PromptTemplate

ollama_llm = OllamaLLM(
    model="llama3.2",
    endpoint="http://127.0.0.1:11434/"
)

prompt_template = """
Odpowiedz na pytanie: {question}
"""
prompt = PromptTemplate(template=prompt_template, input_variables=["question"])
chain = prompt | ollama_llm

question = "Podaj przepis na rosół"
response = chain.invoke({"question": question})

print(f"Pytanie: {question}")
print(f"Odpowiedź: {response.text if hasattr(response, 'text') else response}")

with open("odpowiedzi.txt", "a", encoding="utf-8") as file:
    file.write(f"Pytanie: {question}\n")
    file.write(f"Odpowiedź: {response.text if hasattr(response, 'text') else response}\n\n")
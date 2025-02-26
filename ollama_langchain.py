from langchain_ollama import OllamaLLM
from langchain.prompts import PromptTemplate

# Używamy dostępnego modelu 'llama3.2:latest'
ollama_llm = OllamaLLM(
    model="llama3.2:latest",  # Zmieniamy nazwę modelu na "llama3.2:latest"
    endpoint="http://127.0.0.1:11434/"  # Lokalne API serwera Ollama
)

# Tworzymy szablon promptu
prompt_template = """
Odpowiedz na pytanie: {question}
"""
prompt = PromptTemplate(template=prompt_template, input_variables=["question"])

# Łączymy szablon promptu z modelem
chain = prompt | ollama_llm

# Definiujemy pytanie
question = "Podaj przepis na rosół"

# Wysyłamy zapytanie do modelu
response = chain.invoke({"question": question})

# Wyświetlamy odpowiedź
print(f"Pytanie: {question}")
print(f"Odpowiedź: {response.text if hasattr(response, 'text') else response}")

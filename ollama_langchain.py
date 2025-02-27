'''Importuje klasę OllamaLLM z biblioteki langchain_ollama, 
która umożliwia integrację modeli Ollama z frameworkiem LangChain.
Importuje klasę PromptTemplate z biblioteki langchain, 
która służy do tworzenia szablonów promptów.'''

from langchain_ollama import OllamaLLM
from langchain.prompts import PromptTemplate

# Używamy dostępnego modelu 'llama3.2:latest' Tworzy instancję klasy OllamaLLM, 
# która będzie komunikować się z modelem llama3.2 poprzez lokalny endpoint Ollama (http://127.0.0.1:11434/).
ollama_llm = OllamaLLM(
    model="llama3.2",  
    endpoint="http://127.0.0.1:11434/"  # Lokalne API serwera Ollama
)

# Definiuje szablon promptu, który zawiera zmienną {question}, a następnie tworzy obiekt PromptTemplate 
# z tym szablonem, wskazując, że "question" jest zmienną wejściową.
prompt_template = """
Odpowiedz na pytanie: {question}
"""
prompt = PromptTemplate(template=prompt_template, input_variables=["question"])

# Tworzy łańcuch (chain) przetwarzania, łącząc szablon promptu z modelem językowym za pomocą operatora 
# potoku (|), co jest składnią LangChain do łączenia komponentów.
chain = prompt | ollama_llm

# Definiuje zmienną question zawierającą treść pytania, które zostanie przekazane do modelu.
question = "Podaj przepis na rosół"

# Wywołuje utworzony łańcuch z argumentem słownikowym, gdzie klucz "question" odpowiada zmiennej w szablonie. 
# Łańcuch podstawi pytanie do szablonu, a następnie wyśle complet prompt do modelu Ollama i zwróci odpowiedź.
response = chain.invoke({"question": question})

# Wyświetla oryginalne pytanie, a następnie odpowiedź modelu. Wykorzystuje sprawdzenie warunkowe, 
# aby obsłużyć dwa możliwe formaty odpowiedzi: jeśli obiekt response ma atrybut 'text', 
# wyświetli response.text, w przeciwnym razie wyświetli cały obiekt response.
print(f"Pytanie: {question}")
print(f"Odpowiedź: {response.text if hasattr(response, 'text') else response}")

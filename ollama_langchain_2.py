'''2. Dodanie obsługi błędów. 
Jeśli serwer Ollama nie działa lub coś pójdzie nie tak, 
kod może się wywalić. Możemy dodać obsługę wyjątków, 
żeby był bardziej niezawodny.  Dlaczego? 
Jeśli serwer nie działa (np. nie uruchomiono Ollama), dostaniesz 
czytelny komunikat o błędzie zamiast niezrozumiałego crasha.'''


from langchain_ollama import OllamaLLM
from langchain.prompts import PromptTemplate


try:
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

except Exception as e:
    print(f"Wystąpił błąd: {e}")
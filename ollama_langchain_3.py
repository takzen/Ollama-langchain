'''3. Interaktywne wprowadzanie pytań.
   Zamiast ustawiać pytanie na sztywno w kodzie, możesz 
   pozwolić użytkownikowi wpisywać własne pytania. 
   Dlaczego? Kod staje się bardziej dynamiczny – możesz 
   zadawać różne pytania bez edytowania kodu.'''


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

while True:
    question = input("Wpisz swoje pytanie (lub 'wyjdź' żeby zakończyć): ")
    if question.lower() == "wyjdź":
        break
    response = chain.invoke({"question": question})
    print(f"Pytanie: {question}")
    print(f"Odpowiedź: {response.text if hasattr(response, 'text') else response}")
    print("-" * 50)
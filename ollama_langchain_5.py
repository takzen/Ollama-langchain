'''5. Dodanie parametrów modelu.
   Możesz dostosować zachowanie modelu, np. ustawić 
   temperaturę (kontroluje kreatywność odpowiedzi).
   Dlaczego? Temperatura pozwala kontrolować, czy o
   dpowiedzi mają być bardziej przewidywalne (niższa wartość) 
   czy bardziej kreatywne (wyższa wartość).'''

from langchain_ollama import OllamaLLM
from langchain.prompts import PromptTemplate

ollama_llm = OllamaLLM(
    model="llama3.2",
    endpoint="http://127.0.0.1:11434/",
    temperature=0.7  # Wartość od 0 (precyzyjne) do 1 (kreatywne)
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
'''Moja propozycja na start
Spróbuj kreatora przepisów kulinarnych – jest prosty, praktyczny i możesz się pobawić danymi. Oto szkic:'''

from langchain_ollama import OllamaLLM
from langchain.prompts import PromptTemplate

# Fake składniki
skladniki = ["pomidor", "makaron", "ser", "oliwa"]

# Inicjalizacja modelu
llm = OllamaLLM(model="llama3.2")

# Prompt
prompt = PromptTemplate(
    input_variables=["skladniki"],
    template="Mając składniki: {skladniki}, zaproponuj prosty przepis."
)

chain = prompt | llm

# Wywołanie
odpowiedz = chain.invoke({"skladniki": ", ".join(skladniki)})
print(odpowiedz)
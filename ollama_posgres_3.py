'''Opcja 3: Prosty plik JSON
Możesz też zasymulować bazę za pomocą pliku JSON, jeśli chcesz coś trwalszego niż słownik, ale bez SQLite.
Co się dzieje?
Dane są przechowywane w formacie JSON (możesz je zapisać do pliku i wczytywać z json.load()).
unkcja pobierz_produkty działa jak w opcji ze słownikiem.'''

import json
from langchain_ollama import OllamaLLM
from langchain.prompts import PromptTemplate

# Fake dane w JSON (możesz zapisać to do pliku i wczytać)
fake_json = '''
[
    {"nazwa": "Laptop", "cena": 3500.00, "kategoria": "Elektronika"},
    {"nazwa": "Myszka", "cena": 50.00, "kategoria": "Elektronika"},
    {"nazwa": "Krzesło", "cena": 200.00, "kategoria": "Meble"}
]
'''
fake_baza = json.loads(fake_json)

# Funkcja udająca zapytanie
def pobierz_produkty(kategoria=None):
    if kategoria:
        return [row for row in fake_baza if row["kategoria"] == kategoria]
    return fake_baza

# Inicjalizacja modelu
llm = OllamaLLM(model="llama3.2")

# Prompt z kontekstem
prompt = PromptTemplate(
    input_variables=["pytanie", "kontekst"],
    template="Na podstawie danych: {kontekst}\nOdpowiedz na pytanie: {pytanie}"
)

# Łączenie promptu z modelem
chain = prompt | llm

# Przykład użycia
kategoria = "Elektronika"
dane = pobierz_produkty(kategoria)
kontekst = "\n".join([f"Nazwa: {row['nazwa']}, Cena: {row['cena']}, Kategoria: {row['kategoria']}" for row in dane])
pytanie = "Który produkt jest najtańszy?"
odpowiedz = chain.invoke({"pytanie": pytanie, "kontekst": kontekst})
print(odpowiedz)
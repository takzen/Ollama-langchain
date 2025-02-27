'''Opcja 1: Prosty słownik jako "fake" baza
Zamiast łączyć się z PostgreSQL, możemy użyć słownika w Pythonie, który będzie udawał tabelę produkty.
Co się dzieje?
fake_baza to lista słowników, która udaje tabelę w bazie danych.
Funkcja pobierz_produkty filtruje dane tak, jakby to było zapytanie SQL.
Reszta kodu działa tak samo, jak z PostgreSQL.'''


from langchain_ollama import OllamaLLM
from langchain.prompts import PromptTemplate

# Fake baza danych w postaci słownika
fake_baza = [
    {"nazwa": "Laptop", "cena": 3500.00, "kategoria": "Elektronika"},
    {"nazwa": "Myszka", "cena": 50.00, "kategoria": "Elektronika"},
    {"nazwa": "Krzesło", "cena": 200.00, "kategoria": "Meble"}
]

# Funkcja udająca zapytanie do bazy
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
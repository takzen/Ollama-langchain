'''Opcja 2: SQLite w pamięci
Jeśli chcesz coś bliższego prawdziwej bazie, ale bez instalacji PostgreSQL, możesz użyć sqlite3 z bazą w pamięci. SQLite jest wbudowane w Pythona, 
więc nie musisz nic dodatkowo instalować.
Co się dzieje?
Tworzymy tymczasową bazę SQLite w pamięci (:memory:).
Kod jest bardzo podobny do tego z PostgreSQL, ale nie wymaga zewnętrznego serwera.
Po zakończeniu programu baza znika, więc nie zostawia śladu.'''

import sqlite3
from langchain_ollama import OllamaLLM
from langchain.prompts import PromptTemplate

# Tworzenie bazy w pamięci
# conn = sqlite3.connect(":memory:")
conn = sqlite3.connect("moja_baza.db")
cursor = conn.cursor()

# Tworzenie tabeli i dodawanie danych
cursor.execute("""
    CREATE TABLE produkty (
        id INTEGER PRIMARY KEY,
        nazwa TEXT,
        cena REAL,
        kategoria TEXT
    )
""")
cursor.executemany("INSERT INTO produkty (nazwa, cena, kategoria) VALUES (?, ?, ?)", [
    ("Laptop", 3500.00, "Elektronika"),
    ("Myszka", 50.00, "Elektronika"),
    ("Krzesło", 200.00, "Meble")
])
conn.commit()

# Funkcja do pobierania danych
def pobierz_produkty(kategoria=None):
    if kategoria:
        cursor.execute("SELECT nazwa, cena, kategoria FROM produkty WHERE kategoria = ?", (kategoria,))
    else:
        cursor.execute("SELECT nazwa, cena, kategoria FROM produkty")
    return cursor.fetchall()

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
kontekst = "\n".join([f"Nazwa: {row[0]}, Cena: {row[1]}, Kategoria: {row[2]}" for row in dane])
pytanie = "Który produkt jest najtańszy?"
odpowiedz = chain.invoke({"pytanie": pytanie, "kontekst": kontekst})
print(odpowiedz)

# Zamknięcie połączenia
conn.close()
# Uruchamianie lokalnego modelu Ollama 3.2 z Langchain

Krótki przewodnik, jak skonfigurować i uruchomić lokalny model Ollama 3.2 z Langchain. Wykorzystaj moc lokalnych modeli językowych z Langchain.

## Wymagania

* **Ollama:** Zainstalowany i uruchomiony ([https://ollama.com/](https://ollama.com/)).
* **Python:** Wersja 3.7+.
* **Biblioteki Python:** `langchain`, `langchain-ollama`.
* **Model Ollama 3.2:** Wymaga około 2 GB miejsca.

## Instalacja i uruchomienie

### 1. Uruchom Ollama i pobierz model Ollama 3.2:
```bash
ollama serve
ollama pull ollama3.2  # Model Ollama 3.2 (2GB)
```

### 2. Utwórz środowisko wirtualne (zalecane):
```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
# venv\Scripts\activate  # Windows
```
Aby wyjść ze środowiska wirtualnego, użyj:
```bash
deactivate
```

### 3. Zainstaluj Langchain i langchain-ollama:
```bash
pip install --upgrade pip
pip install -U langchain langchain-ollama
```

### 4. Utwórz plik `ollama_langchain.py`:
```python
from langchain_ollama import OllamaLLM
from langchain.prompts import PromptTemplate

ollama_llm = OllamaLLM(model="ollama3.2")  # Model Ollama 3.2

prompt_template = """
Odpowiedz na pytanie: {question}
"""
prompt = PromptTemplate(template=prompt_template, input_variables=["question"])

chain = prompt | ollama_llm

question = "Jaka jest stolica Polski?"
response = chain.invoke({"question": question})

print(f"Pytanie: {question}")
print(f"Odpowiedź: {response.text if hasattr(response, 'text') else response}")
```

### 5. Uruchom kod:
```bash
python ollama_langchain.py
```

## Kod - wyjaśnienie

* `langchain-ollama.OllamaLLM`: Integracja Langchain z Ollama.
* `langchain.prompts.PromptTemplate`: Szablon promptu.
* `prompt | ollama_llm`: Łańcuch Langchain (Runnable Sequence API).
* `chain.invoke({"question": question})`: Uruchomienie łańcucha.

## Co dalej?

* Eksperymentuj z modelem Ollama 3.2 (`ollama pull ollama3.2`).
* Zmieniaj prompty.
* Wykorzystaj zaawansowane funkcje Langchain.
* Dokumentacja Langchain: [https://python.langchain.com/docs/](https://python.langchain.com/docs/)

## Rozwiązywanie problemów

* Serwer Ollama (`ollama serve`) musi działać.
* Model Ollama 3.2 musi być pobrany (`ollama pull ollama3.2`).
* Sprawdź instalację bibliotek (`pip install`).

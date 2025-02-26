import requests

# Ustawienie endpointa Ollama API
url = "http://127.0.0.1:11434/v1/models"  # Zmieniamy na odpowiedni endpoint

# Wysłanie zapytania GET do Ollama API
response = requests.get(url)

# Sprawdzenie, czy zapytanie zakończyło się sukcesem
if response.status_code == 200:
    models = response.json()
    print("Dostępne modele:")
    for model in models['data']:
        print(f"- {model['id']}")
else:
    print(f"Nie udało się uzyskać listy modeli. Status kod: {response.status_code}")

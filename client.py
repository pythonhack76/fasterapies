# client.py
import requests

base_url = "http://127.0.0.1:8000"

# Creare un nuovo articolo
new_item = {"id": 1, "name": "Laptop", "price": 999.99}
response = requests.post(f"{base_url}/items/", json=new_item)

if response.status_code == 200:
    print("Item creato con successo:", response.json())
else:
    print("Errore nella creazione dell'item:", response.status_code)

# Recuperare tutti gli articoli
response = requests.get(f"{base_url}/items/")

if response.status_code == 200:
    items = response.json()
    print("Items recuperati:", items)
else:
    print("Errore nel recupero degli items:", response.status_code)

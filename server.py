# server.py
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    id: int
    name: str
    price: float

items = []

@app.post("/items/")
def create_item(item: Item):
    items.append(item)
    return item

@app.get("/items/")
def read_items():
    return items
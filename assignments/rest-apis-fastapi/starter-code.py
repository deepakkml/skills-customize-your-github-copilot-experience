from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    id: int
    name: str
    description: str | None = None

items: list[Item] = []

@app.get("/items")
def list_items():
    return items

@app.post("/items", status_code=201)
def create_item(item: Item):
    items.append(item)
    return item

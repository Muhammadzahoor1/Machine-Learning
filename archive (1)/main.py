from fastapi import FastAPI

app = FastAPI()

items = []

@app.get("/items")
def get_items():
    return items

@app.post("/items")
def add_item(item: dict):
    items.append(item)
    return {"message": "Item added", "item": item}

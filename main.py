from typing import Optional
from typing import Union

from fastapi import FastAPI, Query
from pydantic import BaseModel

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.get("/items/")
async def read_items(q: Optional[str] = Query(None, min_length=3, max_length=5)):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}


class Payment(BaseModel):
    date: str
    amount: float
    ReceiverAcc: str
    description: Optional[str] = None


d = {}


@app.get("/payments")
def read_item():
    return d


@app.get("/payments/{payment_id}")
def read_item(payment_id: int, q: Union[str, None] = None):
    return {"payment_id": payment_id, "q": q}


@app.put("/payments/{payment_id}")
def update_item(payment_id: int, payment: Payment):
    d[payment_id] = payment.dict()
    return payment.dict()

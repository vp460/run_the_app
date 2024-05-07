from pprint import pprint

from app.db import BaseModel

class Order(BaseModel):

    SHEET_NAME = "orders"

    COLUMNS = ["user_email", "painting_id", "painting_title", "painting_price"]

    SEEDS = []


if __name__ == "__main__":

    orders = Order.all()
    print("FOUND", len(orders), "ORDERS")
    for order in orders:
        pprint(dict(order))

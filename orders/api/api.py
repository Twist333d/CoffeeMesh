# import necessary libraries
from datetime import datetime
from uuid import UUID
from starlette.responses import Response
from starlette import status
from http import HTTPStatus

# create dummy object orders to work with
orders = []
""" 
orders = {
    'id' : 'ff0f1355-e821-4178-9567-550dec27a373',
    'status' : 'delivered',
    'created' : datetime.utcnow(),
    'updated': datetime.utcnow(),
    'order' : [
        {
            'product' : 'capuccino',
            'size' : 'medium',
            'quantity' : 1
        }
    ]
}"""


# create API endpoints
from orders.app import app
from orders.api.schemas import (
    GetOrderSchema, CreateOrderSchema, OrderItemSchema)


@app.get('/orders', response_model=GetOrderSchema) # get a list of orders
def get_orders():
    return {'orders' : [orders]}

@app.post('/orders', # create an order
          status_code=status.HTTP_201_CREATED,
          response_model=CreateOrderSchema)

def create_order(order_details: CreateOrderSchema):
    return get_orders

@app.get('/orders/{order_id}', response_model=GetOrderSchema) # get info of an order
def get_order(order_id: UUID):
    return order

@app.put('/orders/{order_id}', response_model=GetOrderSchema) # update order info
def update_order(order_id: UUID, order_details: CreateOrderSchema):
    return order

@app.delete('/orders/{order_id}') # detele an order
def delete_order(order_id: UUID):
    return Response(status_code=HTTPStatus.NO_CONTENT.value)

@app.post('/orders/{order_id}/cancel', response_model=CreateOrderSchema) # cancel an order
def cancel_order(order_id: UUID):
    return order
"""
Here we'll implement validation models for the API we are building.
"""
# import necessary libraries
from enum import Enum
from typing import List, Optional
from uuid import UUID
from datetime import datetime

from pydantic import BaseModel, Field, conlist, conint, field_validator

# define pydantic classes for each property and schema

class Size(Enum):
    small = 'small',
    medium = 'medium',
    large = 'big'

class Status(Enum):
    created = 'created',
    progress = 'progress',
    cancelled = 'cancelled'
    dispatched = 'dispatched'
    delivered = 'delivered'
    paid = 'paid'

class OrderItemSchema(BaseModel):
    product: str
    size: Size
    quantity: Optional[conint(ge=1, strict=True)] = 1

    @field_validator('quantity')
    def prevent_quantity_null(cls, value):
        assert value is not None, 'Quantity may not be None'
        return value

class CreateOrderSchema(BaseModel):
    order: List[OrderItemSchema] = Field(..., min_items=1)

class GetOrderSchema(CreateOrderSchema):
    id: UUID
    created: datetime
    status: Status
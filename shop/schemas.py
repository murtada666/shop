from decimal import Decimal
from sqlite3 import Date
import uuid
from pydantic import UUID4
from ninja import Schema
from typing import List

class CategoryOut(Schema):
    #parent: "CategoryOut"
    name: str
    description: str = None
    image: str = None
    is_active: bool = True
    children: List["CategoryOut"]
    
    
    
CategoryOut.update_forward_refs()

class AddressIn(Schema):
    name: str
    city: str
    town: str
    address: str
    x: Decimal
    y: Decimal
    phone: str
    
class AddressOut(Schema):
    user: str = None
    city: str
    town: str
    address: str
    x: Decimal
    y: Decimal
    phone: str
    
class ProductIn(Schema):
    id: int
    parent: CategoryOut
    name: str
    weight: str
    cost: int
    desc: str
    image: str
    is_active: bool = True
    
class ProductOut(Schema):
    id: int
    category : CategoryOut
    name: str
    weight: float
    price: int
    description: str
    image: str
    
class Item(Schema):
    id: int
    name: str
    weight: str
    cost: int
    image: str
  
class OrderIn(Schema):
    id: int
    address: AddressOut
    item: List[Item] = None
    note: str = None
    ref_code: str = None
    cost: int
  
class OrderOut(Schema):
    id: int
    address: AddressOut
    item: List[Item] = None
    note: str = None
    ref_code: str = None
    delivery_fee: int = 1500
    cost: int
    date: str = Date
    
class AccountOut(Schema):
    id: int
    name: str
    orders: List[OrderOut] = None
    phone_number: int

class AccountIn(Schema):
    first_name: str
    last_name: str
    user_name: str
    password1: str
    password2: str
    phone_number: int = None
    email: str = None
    

class categoryFilterOut(Schema):
    name: str
    description: str
    products: List[ProductOut]
    
    
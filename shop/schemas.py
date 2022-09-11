from decimal import Decimal
from sqlite3 import Date
from pydantic import UUID4
from ninja import Schema
from typing import List

class Category(Schema):
    name: str
    desc: str
    image: str
    is_active: bool = True

class AddressIn(Schema):
    work_address: bool = False
    city: str
    town: str
    address: str
    x: Decimal
    y: Decimal
    phone: str
    
class AddressOut(Schema):
    user: str = None
    work_address: bool = False
    city: str
    town: str
    address: str
    x: Decimal
    y: Decimal
    phone: str
    
class ProductIn(Schema):
    id: UUID4
    parent: Category
    name: str
    weight: str
    cost: int
    desc: str
    image: int
    is_active: bool = True
    
class ProductOut(Schema):
    id: UUID4
    parent: Category
    name: str
    weight: str
    cost: int
    desc: str
    image: str
    
class Item(Schema):
    id: ProductOut.id
    name: str
    weight: str
    cost: int
    image: str
  
class OrderIn(Schema):
    id: UUID4
    address: AddressOut
    item: List[Item] = None
    note: str = None
    ref_code: str = None
    cost: int
  
class OrderOut(Schema):
    id: OrderIn.id
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
    

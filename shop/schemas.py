from decimal import Decimal
from sqlite3 import Date
from ninja import Schema
from typing import List

class CategoryOut(Schema):
    name: str
    description: str = None
    image: str = None
    is_active: bool = True
    children: List["CategoryOut"]
    
    
    
CategoryOut.update_forward_refs()

class UserName(Schema):
    name: str
    
class Town(Schema):
    city: str
    Town: str

    
class AddressIn(Schema):
    user: UserName
    name: str
    town: Town
    address: str 
    x: Decimal = None
    y: Decimal = None
    phone: str
   
class AddressOut(Schema):
    user: UserName
    town: Town
    address: str
    x: Decimal = None
    y: Decimal = None
    phone: str
    
class ProductIn(Schema):
    id: int
    parent: CategoryOut
    name: str
    weight: float
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
    
class ProductToItem(Schema):
    name: str

class AddressToOrder(Schema):
    name: str
    town: Town
        
class Items(Schema):
    id: int
    product: ProductToItem
    item_qty: int = 0
    # weight: str
    # cost: int
    # image: str
  
class OrderIn(Schema):
    user: UserName
    address: AddressToOrder
    items: List[Items] = None
    note: str = None
    ref_code: str = None
    delivery_fee: int = 1500
    cost: int = 0
  
class OrderOut(Schema):
    id: int
    address: AddressOut
    items: List[Items] = None
    note: str = None
    ref_code: str = None
    delivery_fee: int = 1500
    cost: int
    total: int
    date: str = Date

class OrderToAccount(Schema):
    id: int
    address: AddressToOrder
    total:int
        
class AccountOut(Schema):
    id: int
    name: UserName
    orders: List[OrderToAccount] = None
    phone_number: int

class categoryFilterOut(Schema):
    name: str
    description: str
    products: List[ProductToItem]
    
    
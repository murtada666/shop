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



class CityOut(Schema):
    name:str
class Town(Schema):
    name: str
    city: CityOut
    
class UserName(Schema):
    first_name: str
    last_name: str
    
class UserNameOut(UserName):
    id: int

class UserNameIn(UserName):
    pass
    


    
class AddressIn(Schema):
    user: UserNameIn
    name: str
    town: Town
    address: str #اقرب نقطة دالة
    #x: Decimal = None
    #y: Decimal = None
    phone: str
   
class AddressOut(Schema):
    user: UserNameOut
    town: Town
    address: str
    #x: Decimal = None
    #y: Decimal = None
    phone: str
    
class ProductIn(Schema):
    parent: CategoryOut
    name: str
    weight: float
    cost: int
    desc: str#/...............y
    image: str
    is_active: bool = True
    
class ProductOut(Schema):
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
    user: UserNameIn
    address: AddressToOrder
    items: List[Items] = None
    note: str = None
    ref_code: str = None
    delivery_fee: int = 1500
    cost: int = 0
  
class OrderOut(Schema):
    id: int
    #user: UserNameOut
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
    name: UserNameOut
    orders: List[OrderToAccount] = None
    phone_number: int

class categoryFilterOut(Schema):
    name: str
    description: str
    products: List[ProductToItem]
    
    
from decimal import Decimal
from sqlite3 import Date
from unicodedata import name
from ninja import Schema
from typing import List


# class CategoryOut(Schema):
#     name: str
#     description: str = None
#     image: str = None
#     is_active: bool = True
#     children: List["CategoryOut"]
    
# CategoryOut.update_forward_refs()

class CategoryOut(Schema):
    name: str
    image: str


class CityOut(Schema):
    name:str = None


class Town(Schema):
    name: str = None
    city: CityOut = None
   
    
class UserName(Schema):
    id: int
    
    
class AddressIn(Schema):
    user: UserName
    name: str
    town: Town
    address: str #اقرب نقطة دالة
    #x: Decimal = None
    #y: Decimal = None
    phone: str
   
   
class AddressOut(Schema):
    user: UserName
    town: Town
    address: str
    #x: Decimal = None
    #y: Decimal = None
    phone: str
    
    
# class ProductIn(Schema):
#     parent: CategoryOut
#     name: str
#     weight: float
#     cost: int
#     desc: str
#     image: str
#     is_active: bool = True
    
class CategoryProductOut(Schema):
    name: str
    is_active: bool = True

class ProductOut(Schema):
    category : CategoryProductOut
    name: str
    #weight: float = None
    price: int
    description: str
    image: str
    
class CardProductOut(Schema):
    name: str
    price: int
    image: str
    
    
class ProductToItem(Schema):
    name: str
    price: int
    image: str
    


class AddressToOrder(Schema):
    name: str
    town: Town
    
        
class ItemIn(Schema):
    user_id:int
    product_id: int
    item_qty: int
    
            
class Items(Schema):
    id: int
    product: ProductToItem
    item_qty: int = 0
  
  
class OrderIn(Schema):
    user: UserName
    address_id: int
    item_id: List[int] = None
    note: str = None
    ref_code: str = None
    delivery_fee: int = 1500
  
  
class OrderOut(Schema):
    id: int
    #user: UserNameOut
    address: AddressOut
    items: List[Items] = None
    note: str = None
    ref_code: str = None
    delivery_fee: int = 1500
    total: int
    date: str = Date


class OrderToAccount(Schema):
    id: int
    address: AddressToOrder
    total:int
      
        
class AccountOut(Schema):
    id: int
    # user: UserNameOut
    orders: List[OrderToAccount] = None
    phone_number: int


class categoryFilterOut(Schema):
    name: str
    description: str
    products: List[ProductToItem]
    
    
class MessageOut(Schema):
    message: str
    
    
class ItemQty(Schema):
    user: UserName
    id: int
    item_qty: int
    
class Favourites(Schema):
    user_id: int
    product: ProductToItem
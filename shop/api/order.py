from typing import List
from ninja import Router
from shop.api.address import user_addresses
from shop.models import Order, Item
from shop.schemas import OrderIn, OrderOut, UserName
from django.shortcuts import get_object_or_404

order_router = Router(tags=["Order endpoints"])

#getting all orders
@order_router.get("all/", response=List[OrderOut])
def getAll(request, user_id: int):
    orders = Order.objects.filter(user_id=user_id).all()

    return orders

#getting all user orders
@order_router.get("get_order/", response=OrderOut)
def user_order(request, user_id: int):
    t = Order.objects.get(user_id=user_id)
    
    return t

#checking if an order exist or not and if not creating a new one
@order_router.post('make_order/', response=OrderOut)
def make_order(request, order_in: OrderIn):
    try:
        order = Order.objects.get(is_ordered=False, user_id=order_in.user.id)
        
        return order
    except:
        t = Order(
            user_id=order_in.user.id,
            address_id=order_in.address_id,
            note=order_in.note,
            ref_code=order_in.ref_code,
            delivery_fee=order_in.delivery_fee,
            )
        t.save()
        t.items.add(*Item.objects.filter(id__in=order_in.item_id).all())
        Item.objects.filter(id__in=order_in.item_id).update(ordered=True)
        t.total = t.order_total
        t.save()
        
        return t

#checking out the order AKA making it ordered
@order_router.post('checkout_order/', response=OrderOut)
def make_order(request, user_id: int):

    return Order.objects.filter(is_ordered=False, user_id=user_id).update(is_ordered=True)

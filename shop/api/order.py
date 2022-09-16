from ninja import Router
from shop.api.address import user_addresses
from shop.models import Order, Item
from shop.schemas import OrderIn,OrderOut, UserName
from django.shortcuts import get_object_or_404

order_router = Router(tags=["Order endpoints"])
@order_router.post('make_order/', response = OrderOut)
def make_order(request, order_in: OrderIn):
    
    
    t = Order(user_id = order_in.user_id,
              address_id = order_in.address_id,
              note = order_in.note,
              ref_code = order_in.ref_code,
              delivery_fee = order_in.delivery_fee,
              cost = order_in.cost)
    t.save()
    
    t.items.add(*Item.objects.filter(id__in = order_in.item_id).all())
    
    t.total = t.order_total
    t.save()
    return t

@order_router.get("get_all/", response= OrderOut)
def user_order(request, user):
    t = Order.objects.get(user = user)
    return t

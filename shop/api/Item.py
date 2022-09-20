from ninja import Router
from shop.schemas import ItemIn, MessageOut
from shop.models import Item
from django.contrib.auth import get_user_model

User = get_user_model()

item_router = Router(tags=["Item Endpoints"])

#creating a new item
@item_router.post("create_item", response={
    201: MessageOut
})
def create_item(request, payload: ItemIn):
    Item.objects.create(
        ordered=False,
        user_id=payload.user_id,
        product_id=payload.product_id,
        item_qty=payload.item_qty
    )
    
    return 201,{'message': "Item created successfully!"}

#updating the quantity of a certain item in cart
@item_router.put("qty/", response= {
    201: MessageOut
})
def update_qty(request, user_id:int,item_id:int, item_qty: int):
    Item.objects.filter(
        user_id=user_id,
        id=item_id,
    ).update(item_qty=item_qty)
    return {"message": "Done!"}

#deleting an item completely from cart
@item_router.delete("delete/", response={201: MessageOut})
def delete_item(request, user_id:int,item_id:int):
    Item.objects.filter(
            user_id=user_id,
            id=item_id,
        ).delete()
    return {"message": "Done!"}

from ninja import Router

order_router = Router(tags=["Order endpoints"])

@order_router.get("user_order/")
def user_order(request, user_id):
    pass

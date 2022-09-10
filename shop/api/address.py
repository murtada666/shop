from ninja import Router

address_router = Router(tags=["Address Endpoints"])



@address_router.get("user_addresses/")
def user_addresses(request, user_id):
    pass


@address_router.post("new_address/")
def new_address(request, user_id):
    pass
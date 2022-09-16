from ninja import Router

from shop.models import Address
from shop.schemas import AddressIn, AddressOut

address_router = Router(tags=["Address Endpoints"])



@address_router.get("user_addresses/", response=AddressOut)
def user_addresses(request, user_id):
    address = Address.objects.get(id=user_id)


@address_router.post("new_address/", response=AddressIn)
def new_address(request, user_id):
    #address = Address.objects.create
    
    pass
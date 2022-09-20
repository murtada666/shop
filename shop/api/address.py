from ast import Try
from cmath import phase
from ninja import Router
from shop.models import Address, City, Town
from shop.schemas import AddressIn, AddressOut

address_router = Router(tags=["Address Endpoints"])

@address_router.get("user_addresses/", response=AddressOut)
def user_addresses(request, user_id):
    address = Address.objects.filter(user_id=user_id).all()
    
    return address

@address_router.post("new_address/")
def new_address(request, address_in: AddressIn):
    userAddress = Address.objects.create(
        user_id=address_in.user_id,
        name=address_in.name,
        town=Town.objects.get_or_create(name=address_in.town)[0],
        address=address_in.address,
        x=address_in.x,
        y=address_in.y,
        phone=address_in.phone
    )
    
    return userAddress

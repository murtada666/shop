from typing import List
from ninja import Router
from shop.models import Address, City, Town
from shop.schemas import AddressIn, AddressOut, MessageOut

address_router = Router(tags=["Address Endpoints"])

@address_router.get("user_addresses/{user_id}", response=List[AddressOut])
def user_addresses(request, user_id):
    address = Address.objects.filter(user_id=user_id).all()
    
    return address

@address_router.post("new_address/", response= MessageOut)
def new_address(request, address_in: AddressIn):
    userAddress = Address.objects.create(
        user_id=address_in.user.id,
        name=address_in.name,
        town=Town.objects.get_or_create(name=address_in.town.name)[0],
        address=address_in.address,
        phone=address_in.phone
    )
    
    return {"message": "Address Created!"}

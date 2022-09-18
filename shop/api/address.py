import tabnanny
from unicodedata import name
from ninja import Router

from shop.models import Address, Town, User
from shop.schemas import AddressIn, AddressOut, UserName

address_router = Router(tags=["Address Endpoints"])



@address_router.get("user_addresses/", response=AddressOut)
def user_addresses(request, user_id: int):
    
    address = Address.objects.get(user_id=user_id)
    
    return address


@address_router.post("new_address/", response=AddressOut)
def new_address(request, address_in: AddressIn):
    t = Address.objects.create(
        #user=address_in.user_id,
        user=User.objects.get(user=UserName.name),
        name=address_in.name,
        #city=address_in.city,
        town=Town.objects.get_or_create(name=address_in.town)[0],
        address=address_in.address,
        #x=address_in.x,
        #y=address_in.y,
        phone=address_in.phone
        )
    return t
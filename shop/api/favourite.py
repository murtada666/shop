from typing import List
from ninja import Router
from shop.models import Favourite
from shop.schemas import Favourites

favourite_router = Router(tags=["Favourites"])

@favourite_router.get("user_fav/", response= List[Favourites])
def make_fav(request, user_id: int):
    t = Favourite.objects.filter(user_id = user_id).all()
    return t
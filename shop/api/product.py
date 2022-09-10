from typing import List
from ninja import Router

from shop.models import Product



product_router = Router(tags=["Products Endpoints"])


@product_router.get("all_proudects/")
def list_all_prodducts(request):
    pass


@product_router.get("product_details/")
def product_detalis(request, product_id):
    pass


@product_router.get("featured_products/")
def featured_products(request):
    pass
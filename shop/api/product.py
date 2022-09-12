from typing import List
from ninja import Router

from shop.models import Product
from shop.schemas import ProductIn, ProductOut




product_router = Router(tags=["Products Endpoints"])


@product_router.get("all_produects/", response=List[ProductOut])
def list_all_prodducts(request):
    products = Product.objects.all()
    print(products)
    #print(Product)
    return 200, products


@product_router.get("product_details/", response=ProductOut)
def product_detalis(request, product_name: str ):
    product = Product.objects.get(name=product_name)
    print(product)
    
    return product


@product_router.get("featured_products/")
def featured_products(request):
    pass
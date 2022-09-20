from typing import List
from ninja import Router
from shop.models import Product
from shop.schemas import ProductOut

product_router = Router(tags=["Products Endpoints"])

#getting all products
@product_router.get("all_products/", response=List[ProductOut])
def list_all_products(request):
    products = Product.objects.all()

    return 200, products

#getting the product by name
@product_router.get("product_details/", response=ProductOut)
def product_detalis(request, product_name: str ):
    product = Product.objects.get(name=product_name)
    
    return product
    
#getting the featured products only    
@product_router.get("featured_products/", response=List[ProductOut])
def featured_products(request):
    featured = Product.objects.filter(is_featured=True)
    
    return featured
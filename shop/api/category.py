from typing import List
from unicodedata import name
from ninja import Router
from shop.models import Category
from shop.schemas import CategoryOut

category_router = Router(tags=["Categories Endpoints"])


@category_router.get("categories/", response=List[CategoryOut])
def all_categories(request):
    
    categories = Category.objects.all()
    
    return categories

@category_router.get("specific_category/", response=List[CategoryOut])
def specific_category(request, category_name: str):
    category = Category.objects.get(name=category_name)
    kids = category.children.all()
    
    print(category)
    return kids
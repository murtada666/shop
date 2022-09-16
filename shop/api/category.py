from typing import List
from ninja import Router
from shop.models import Category
from shop.schemas import CategoryOut, categoryFilterOut
from django.shortcuts import get_object_or_404


category_router = Router(tags=["Categories Endpoints"])


@category_router.get("categories/", response=List[CategoryOut])
def all_categories(request):
    
    categories = Category.objects.all()
    
    return categories

@category_router.get("specific_category/", response=CategoryOut)
def specific_category(request, category_name):
    #category = Category.objects.get(name=category_name)
    #sub_category = Category.children.get(name=category_name)
    category  = get_object_or_404(Category , name=category_name)
    #sub_category = category.children.all()
    
    #print(category)
    return category

@category_router.get("filter/", response=categoryFilterOut)
def filter(request, category_name):
    category  = get_object_or_404(Category , name=category_name)
    
    return category
from ninja import Router

category_router = Router(tags=["Categories Endpoints"])


@category_router.get("categories/")
def all_categories(request):
    pass

@category_router.get("specific_category/")
def specific_category(request, category_id):
    pass
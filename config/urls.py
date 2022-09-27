from django.contrib import admin
from django.urls import path,include
from ninja import NinjaAPI
from shop.api.product import product_router
from shop.api.order import order_router
from shop.api.Item import item_router
from shop.api.category import category_router
from shop.api.address import address_router
from shop.api.favourite import favourite_router
api = NinjaAPI(
    title="stop & shop API"
)

api.add_router("category/",category_router)
api.add_router("product/", product_router)
api.add_router("item/", item_router)
api.add_router("address/",address_router)
api.add_router("order/", order_router)
api.add_router("product/", favourite_router)

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/", api.urls),
    path('accounts/', include('allauth.urls')),
]

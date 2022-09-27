from django.contrib import admin
from django.urls import path,include
from ninja import NinjaAPI
from shop.api.product import product_router
from shop.api.order import order_router
from shop.api.Item import item_router
from shop.api.category import category_router
from shop.api.address import address_router
from shop.api.favourite import favourite_router

from config import settings
from django.conf.urls.static import static

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
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from ninja import NinjaAPI  


from shop.api.product import product_router
from shop.api.order import order_router
from shop.api.Item import item_router
from shop.api.category import category_router
from shop.api.city import city_router
from shop.api.address import address_router
from shop.api.town import town_router
api = NinjaAPI()

api.add_router("product/", product_router)
api.add_router("order/", order_router)
api.add_router("item/", item_router)
api.add_router("category/",category_router)
api.add_router("city/",city_router)
api.add_router("town/",town_router)
api.add_router("address/",address_router)



urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/", api.urls),
]

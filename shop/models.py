import datetime
import uuid
from django.db import models
from django.contrib.auth import get_user_model
from ckeditor.fields import RichTextField
from mptt.models import MPTTModel
User = get_user_model()

class Entity(models.Model):
    class Meta:
        abstract = True #we are telling ORM not to create a table for this class in the DB.

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created = models.DateTimeField(editable=False, auto_now_add=True)
    updated = models.DateTimeField(editable=False, auto_now=True)
    

class Category(Entity):
    class Meta:
        verbose_name_plural = "categories"
    
    parent = models.ForeignKey('self', verbose_name='parent', related_name='children',
                            null=True,
                            blank=True,
                            on_delete=models.CASCADE, default=0)
    name = models.CharField('name', max_length=255)
    description = models.TextField('description', null=True, blank= True)
    is_active = models.BooleanField('is active')
    image = models.ImageField('image', upload_to='category/', default="", null=True, blank= True)
    def __str__(self):
        if self.parent:
            return f'{self.name}'
        return f'{self.name}'
    
    
class Product(Entity):
    name = models.CharField('name', max_length=255)
    description = RichTextField('description', null=True, blank=True)
    weight = models.FloatField('weight', null=True, blank=True)
    price = models.IntegerField('price')
    discounted_price = models.IntegerField('discounted price', default = 0)
    image = models.ImageField('image', upload_to='product/', default ="")
    category = models.ForeignKey(Category, verbose_name='category', related_name='products',
                                 null=True,
                                 blank=True,
                                 on_delete=models.SET_NULL,
                                 default=0)
    is_active = models.BooleanField('is active', default=True) # in case we wanted to make soft delete 


    def __str__(self):
        return self.name
    
class Item(Entity):
    """
    Product can live alone in the system, while
    Item can only live within an order
    """
    user = models.ForeignKey(User, verbose_name='user', related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, verbose_name='product',
                                on_delete=models.CASCADE)
    item_qty = models.IntegerField('item_qty')
    ordered = models.BooleanField('ordered')

    def __str__(self):
        return f'{self.product.name}'
    
    
    
class Order(Entity):
    user = models.ForeignKey(User, verbose_name='user', related_name='orders', null=True, blank=True,
                             on_delete=models.CASCADE)
    address = models.ForeignKey("Address", verbose_name='address', null=True, blank=True,
                                on_delete=models.CASCADE)
    date = models.DateField(default=datetime.datetime.today)
    
    note = models.CharField('note', null=True, blank=True, max_length=255)
    ref_code = models.CharField('ref code', max_length=255)
    is_ordered = models.BooleanField('ordered', default= False)
    is_canceled = models.BooleanField('canceled', default= False)
    is_pending = models.BooleanField('pending', default= False)
    items = models.ManyToManyField(Item, verbose_name='items', related_name='order')
    total = models.CharField('total', max_length=255, default= None)

    def __str__(self):
        return f'{self.user.first_name} + {self.total}'

    @property
    def order_total(self):
        order_total = sum(
           (i.product.price-i.product.price_discounted) * i.item_qty for i in self.items.all()
        )

        return order_total
    
    
    
    
class City(Entity):
    name = models.CharField('المحافظة', max_length=255)

    def __str__(self):
        return self.name
    
    
class Town(Entity):
    name = models.CharField('المدينة', max_length=255)
    city = models.ForeignKey(City, related_name='cities', on_delete=models.CASCADE, null=True, blank=True)
    
    def __str__(self):
        return self.name


class Address(Entity):
    user = models.ForeignKey(User, verbose_name='user', related_name='address',
                             on_delete=models.CASCADE)
    name = models.CharField('address name', max_length=255, default="user")
    town = models.ForeignKey(Town, related_name='towns', on_delete=models.CASCADE, null=True, blank=True)
    address = models.CharField('address', max_length=255, null=True, blank=True)
    x = models.CharField('x_coord', max_length=255, null=True, blank=True)
    y = models.CharField('y_coord', max_length=255, null=True, blank=True)
    phone = models.CharField('phone number', max_length=255)

    def __str__(self):
        return f'{self.user.first_name}- {self.address} - {self.town} - {self.town.city} - {self.phone}'

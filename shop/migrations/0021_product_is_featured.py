# Generated by Django 4.1.1 on 2022-09-13 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0020_address_ud_category_ud_city_ud_item_ud_order_ud_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='is_featured',
            field=models.BooleanField(default=False, verbose_name='is featured'),
        ),
    ]

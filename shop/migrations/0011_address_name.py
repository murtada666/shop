# Generated by Django 4.1.1 on 2022-09-11 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0010_alter_category_name_alter_product_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='name',
            field=models.CharField(default='user', max_length=255, verbose_name='address name'),
        ),
    ]

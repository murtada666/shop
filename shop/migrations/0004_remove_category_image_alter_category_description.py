# Generated by Django 4.1.1 on 2022-09-09 11:01

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_remove_address_city_town_city'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='image',
        ),
        migrations.AlterField(
            model_name='category',
            name='description',
            field=ckeditor.fields.RichTextField(verbose_name='description'),
        ),
    ]
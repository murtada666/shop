# Generated by Django 4.1.1 on 2022-09-11 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0008_alter_category_description_alter_category_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.TextField(max_length=255, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.TextField(max_length=255, verbose_name='name'),
        ),
    ]

# Generated by Django 4.1.1 on 2022-09-17 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0022_rename_ud_address_uid_rename_ud_category_uid_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='address',
            name='x',
        ),
        migrations.RemoveField(
            model_name='address',
            name='y',
        ),
        migrations.AlterField(
            model_name='address',
            name='address',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='اقرب نقطة دالة'),
        ),
    ]

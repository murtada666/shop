# Generated by Django 4.1.1 on 2022-09-16 01:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0021_product_is_featured'),
    ]

    operations = [
        migrations.RenameField(
            model_name='address',
            old_name='ud',
            new_name='uid',
        ),
        migrations.RenameField(
            model_name='category',
            old_name='ud',
            new_name='uid',
        ),
        migrations.RenameField(
            model_name='city',
            old_name='ud',
            new_name='uid',
        ),
        migrations.RenameField(
            model_name='item',
            old_name='ud',
            new_name='uid',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='ud',
            new_name='uid',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='ud',
            new_name='uid',
        ),
        migrations.RenameField(
            model_name='town',
            old_name='ud',
            new_name='uid',
        ),
        migrations.AddField(
            model_name='order',
            name='cost',
            field=models.IntegerField(default=0, verbose_name='cost'),
        ),
        migrations.AddField(
            model_name='order',
            name='delivery_fee',
            field=models.IntegerField(default=1500, verbose_name='df'),
        ),
        migrations.AlterField(
            model_name='order',
            name='ref_code',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='ref code'),
        ),
        migrations.AlterField(
            model_name='order',
            name='total',
            field=models.IntegerField(default=0, verbose_name='total'),
        ),
    ]
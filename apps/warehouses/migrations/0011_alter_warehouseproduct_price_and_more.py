# Generated by Django 4.2.6 on 2024-06-14 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('warehouses', '0010_warehouse_icon_warehouse_is_view_warehouse_unit_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='warehouseproduct',
            name='price',
            field=models.IntegerField(blank=True, null=True, verbose_name='цена'),
        ),
        migrations.AlterField(
            model_name='warehouseproduct',
            name='weight',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]

# Generated by Django 4.2.6 on 2024-06-30 04:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('countries', '0001_initial'),
        ('my_warehouse', '0003_mywarehouse_country_of_destination_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='mywarehouse',
            name='city_warehouse',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='city_warehouse_warehouseproducts', to='countries.country'),
        ),
    ]

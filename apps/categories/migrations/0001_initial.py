# Generated by Django 4.2.9 on 2024-03-22 00:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('codename', models.CharField(blank=True, max_length=255, null=True, unique=True)),
                ('icon', models.ImageField(upload_to='category_icons/')),
            ],
        ),
    ]

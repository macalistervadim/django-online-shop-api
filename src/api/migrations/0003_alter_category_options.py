# Generated by Django 5.1.5 on 2025-01-30 09:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_rename_product_cart_product_id'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'category', 'verbose_name_plural': 'categories'},
        ),
    ]

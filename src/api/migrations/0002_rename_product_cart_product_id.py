# Generated by Django 5.1.5 on 2025-01-28 07:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cart',
            old_name='product',
            new_name='product_id',
        ),
    ]

# Generated by Django 4.1.3 on 2023-06-06 10:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_order_billing_address_alter_order_shipping_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartproduct',
            name='cart',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cartproduct', to='products.cart'),
        ),
        migrations.AlterField(
            model_name='cartproduct',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product', to='products.product'),
        ),
    ]

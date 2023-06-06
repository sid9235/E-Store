# Generated by Django 4.1.3 on 2022-12-02 05:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_rename_profile_pic_customer_image'),
        ('products', '0007_alter_product_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='billing_address',
            field=models.ForeignKey(blank=True, limit_choices_to={'address_type': 'bill'}, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='pbill', to='account.customeraddress'),
        ),
        migrations.AlterField(
            model_name='order',
            name='shipping_address',
            field=models.ForeignKey(blank=True, limit_choices_to={'address_type': 'ship'}, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='pship', to='account.customeraddress'),
        ),
    ]

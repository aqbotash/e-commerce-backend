# Generated by Django 5.0 on 2023-12-14 04:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecoMarketAPI', '0010_remove_order_products_alter_orderitem_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_number',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
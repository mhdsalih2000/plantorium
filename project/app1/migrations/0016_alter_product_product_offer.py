# Generated by Django 4.2.1 on 2023-06-16 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0015_product_product_offer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_offer',
            field=models.PositiveBigIntegerField(default=0, null=True),
        ),
    ]

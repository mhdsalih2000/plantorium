# Generated by Django 4.2.1 on 2023-06-08 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0009_alter_category_category_offer_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='category_offer_description',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]

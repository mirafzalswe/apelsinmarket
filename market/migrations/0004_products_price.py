# Generated by Django 5.0 on 2023-12-28 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0003_alter_products_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='price',
            field=models.IntegerField(default=100),
            preserve_default=False,
        ),
    ]
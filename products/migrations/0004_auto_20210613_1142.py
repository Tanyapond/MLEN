# Generated by Django 3.2.4 on 2021-06-13 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_remove_product_image_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='lash_length_and_curl',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='product',
            name='lash_line_length',
            field=models.TextField(blank=True),
        ),
    ]

# Generated by Django 3.2 on 2021-04-29 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='img',
            field=models.ImageField(null=True, upload_to='product-img'),
        ),
    ]

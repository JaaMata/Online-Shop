# Generated by Django 3.2 on 2021-05-13 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0007_auto_20210513_2138'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='tag',
        ),
        migrations.AddField(
            model_name='product',
            name='tag',
            field=models.ManyToManyField(null=True, to='dashboard.Tag'),
        ),
    ]

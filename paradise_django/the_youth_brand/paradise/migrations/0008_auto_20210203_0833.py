# Generated by Django 3.0.6 on 2021-02-03 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paradise', '0007_auto_20210203_0814'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.SlugField(),
        ),
    ]
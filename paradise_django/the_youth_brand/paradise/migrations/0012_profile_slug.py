# Generated by Django 3.0.6 on 2021-02-03 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paradise', '0011_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='slug',
            field=models.SlugField(null=True, unique=True),
        ),
    ]
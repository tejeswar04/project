# Generated by Django 5.1.2 on 2025-01-19 15:53

import blogs.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogs',
            name='img',
            field=models.ImageField(storage=blogs.models.TableBasedStorage(table_name='blogs'), upload_to=''),
        ),
    ]

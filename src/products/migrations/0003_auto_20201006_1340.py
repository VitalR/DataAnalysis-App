# Generated by Django 3.1.2 on 2020-10-06 13:40

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_purchase'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]

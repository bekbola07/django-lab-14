# Generated by Django 5.0 on 2024-12-09 16:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_remove_buy_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='buy',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='store.product'),
        ),
    ]

# Generated by Django 4.0 on 2022-10-20 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_total',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='order',
            name='tax',
            field=models.FloatField(),
        ),
    ]

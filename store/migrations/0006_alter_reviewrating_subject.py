# Generated by Django 4.0 on 2022-11-03 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_alter_product_description_alter_reviewrating_subject'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviewrating',
            name='subject',
            field=models.CharField(blank=True, error_messages={'max_length': 'Too long'}, max_length=128),
        ),
    ]
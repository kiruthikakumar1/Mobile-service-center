# Generated by Django 5.0.2 on 2024-05-02 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('serviceapp', '0004_alter_order_odprocolor_alter_order_odproprice_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='odcomname',
            field=models.CharField(default=True, max_length=150),
        ),
    ]

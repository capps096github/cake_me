# Generated by Django 4.1.1 on 2022-09-29 09:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cake_me_app', '0009_orderitem_order'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderitem',
            name='order',
        ),
    ]

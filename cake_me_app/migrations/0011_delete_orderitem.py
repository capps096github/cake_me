# Generated by Django 4.1.1 on 2022-09-29 09:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cake_me_app', '0010_remove_orderitem_order'),
    ]

    operations = [
        migrations.DeleteModel(
            name='OrderItem',
        ),
    ]

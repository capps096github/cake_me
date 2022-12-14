# Generated by Django 4.1.1 on 2022-09-29 10:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cake_me_app', '0017_remove_cakeorderitem_order_delete_order'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_cost', models.FloatField(default=0, help_text='Enter the total cost of the order')),
                ('date', models.DateField(default=django.utils.timezone.now, help_text='Enter the date of the order')),
                ('order_items', models.ManyToManyField(to='cake_me_app.cakeorderitem')),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

# Generated by Django 4.1.1 on 2022-09-29 09:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cake_me_app', '0012_orderitem'),
    ]

    operations = [
        migrations.CreateModel(
            name='CakeOrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=0, help_text='Enter the quantity of the cake')),
                ('cake', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='cake_me_app.cake')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cake_me_app.order')),
            ],
        ),
        migrations.DeleteModel(
            name='OrderItem',
        ),
    ]

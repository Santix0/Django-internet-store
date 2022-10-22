# Generated by Django 4.1 on 2022-10-18 13:44

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shopping_cart', '0014_alter_checkout_user_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='checkout',
            name='products',
            field=models.ManyToManyField(to='shopping_cart.order'),
        ),
        migrations.AlterField(
            model_name='checkout',
            name='user_id',
            field=models.ManyToManyField(blank=True, null=True, to=settings.AUTH_USER_MODEL),
        ),
    ]

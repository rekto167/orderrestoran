# Generated by Django 3.1.5 on 2021-02-11 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restoran', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='menuorder',
            name='order_complete',
            field=models.BooleanField(default=False),
        ),
    ]
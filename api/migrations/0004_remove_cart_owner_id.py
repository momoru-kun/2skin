# Generated by Django 3.2.3 on 2021-05-27 23:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20210527_2321'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='owner_id',
        ),
    ]

# Generated by Django 2.2.5 on 2019-09-11 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service_providers', '0007_auto_20190911_0918'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deliveryconfirmed',
            name='condition_comment',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='dockconfirmed',
            name='condition_comment',
            field=models.CharField(max_length=50),
        ),
    ]

# Generated by Django 3.0.7 on 2020-08-17 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0030_auto_20200709_1855'),
    ]

    operations = [
        migrations.AddField(
            model_name='contragent',
            name='type_info',
            field=models.CharField(max_length=100, null=True),
        ),
    ]

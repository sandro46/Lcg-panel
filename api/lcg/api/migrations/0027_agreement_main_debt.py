# Generated by Django 3.0.4 on 2020-05-10 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0026_auto_20200510_1101'),
    ]

    operations = [
        migrations.AddField(
            model_name='agreement',
            name='main_debt',
            field=models.FloatField(default=0),
        ),
    ]
# Generated by Django 3.0.2 on 2020-02-18 11:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_auto_20200217_1518'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer_phone',
            name='customer',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='api.Customer'),
            preserve_default=False,
        ),
    ]
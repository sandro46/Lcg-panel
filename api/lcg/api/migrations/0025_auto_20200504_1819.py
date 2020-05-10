# Generated by Django 3.0.4 on 2020-05-04 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0024_auto_20200430_1116'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='end_commission',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='payment',
            name='end_court_costs',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='payment',
            name='end_main_debt',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='payment',
            name='end_penalty',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='payment',
            name='end_percent',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='payment',
            name='start_commission',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='payment',
            name='start_court_costs',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='payment',
            name='start_main_debt',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='payment',
            name='start_penalty',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='payment',
            name='start_percent',
            field=models.FloatField(null=True),
        ),
    ]
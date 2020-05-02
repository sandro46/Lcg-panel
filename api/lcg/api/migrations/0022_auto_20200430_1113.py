# Generated by Django 3.0.4 on 2020-04-30 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0021_auto_20200430_1112'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='commission_end',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='payment',
            name='commission_start',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='payment',
            name='court_costs_end',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='payment',
            name='court_costs_start',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='payment',
            name='main_debt_end',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='payment',
            name='main_debt_start',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='payment',
            name='penalty_end',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='payment',
            name='penalty_start',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='payment',
            name='percent_end',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='payment',
            name='percent_start',
            field=models.FloatField(default=0),
        ),
    ]

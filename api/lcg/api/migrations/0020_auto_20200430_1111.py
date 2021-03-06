# Generated by Django 3.0.4 on 2020-04-30 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0019_auto_20200430_1026'),
    ]

    operations = [
        migrations.RenameField(
            model_name='payment',
            old_name='commission',
            new_name='commission_end',
        ),
        migrations.RenameField(
            model_name='payment',
            old_name='court_costs',
            new_name='commission_start',
        ),
        migrations.RenameField(
            model_name='payment',
            old_name='main_debt',
            new_name='court_costs_end',
        ),
        migrations.RenameField(
            model_name='payment',
            old_name='penalty',
            new_name='court_costs_start',
        ),
        migrations.RenameField(
            model_name='payment',
            old_name='percent',
            new_name='main_debt_end',
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

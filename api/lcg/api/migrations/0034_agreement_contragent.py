# Generated by Django 3.0.7 on 2020-08-19 10:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0033_remove_agreement_contragent'),
    ]

    operations = [
        migrations.AddField(
            model_name='agreement',
            name='contragent',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.Contragent'),
        ),
    ]

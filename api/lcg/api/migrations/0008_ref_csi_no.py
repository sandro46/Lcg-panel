# Generated by Django 3.0.2 on 2020-02-15 22:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_auto_20200215_2205'),
    ]

    operations = [
        migrations.AddField(
            model_name='ref_csi',
            name='no',
            field=models.CharField(max_length=12, null=True),
        ),
    ]

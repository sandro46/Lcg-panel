# Generated by Django 3.0.7 on 2021-01-15 14:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0037_csi_actions_created'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='csi_actions',
            name='give_csi_dt',
        ),
        migrations.RemoveField(
            model_name='csi_actions',
            name='recall_csi_dt',
        ),
        migrations.RemoveField(
            model_name='csi_actions',
            name='return_ispol_doc_dt',
        ),
        migrations.RemoveField(
            model_name='csi_actions',
            name='stop_actions_csi_dt',
        ),
    ]

# Generated by Django 3.0.2 on 2020-02-15 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_delete_ref_process_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ref_process_type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
    ]

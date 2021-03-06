# Generated by Django 3.0.2 on 2020-02-15 21:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Agreement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('agreement_no', models.CharField(max_length=50)),
                ('agreement_from', models.DateField()),
                ('current_debt', models.FloatField(default=0)),
                ('main_debt', models.FloatField(default=0)),
                ('initial_debt', models.FloatField(default=0)),
                ('percent', models.FloatField(default=0)),
                ('commission', models.FloatField(default=0)),
                ('penalty', models.FloatField(default=0)),
                ('product_type', models.CharField(max_length=255, null=True)),
                ('fio_csi', models.CharField(max_length=100, null=True)),
                ('phone_csi', models.CharField(max_length=12, null=True)),
                ('arrest_of_salary', models.CharField(default='N', max_length=1)),
                ('arrest_of_property', models.CharField(default='N', max_length=1)),
                ('arrest_of_accounts', models.CharField(default='N', max_length=1)),
                ('arrest_of_deparure', models.CharField(default='N', max_length=1)),
                ('created', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Contragent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inn', models.CharField(max_length=20)),
                ('f', models.CharField(max_length=50)),
                ('i', models.CharField(max_length=50)),
                ('o', models.CharField(max_length=50, null=True)),
                ('dr', models.DateField(null=True)),
                ('doc_no', models.CharField(max_length=50, null=True)),
                ('address_live', models.IntegerField(null=True)),
                ('address_reg', models.IntegerField(null=True)),
                ('main_phone', models.IntegerField(null=True)),
                ('created', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Ispol_nadpis',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notary_id', models.IntegerField()),
                ('initial_date', models.DateField(null=True)),
                ('start_date', models.DateField(null=True)),
                ('created', models.DateField(auto_now_add=True)),
                ('agreement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Agreement')),
            ],
        ),
        migrations.CreateModel(
            name='Ref_address_type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Ref_load_status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Ref_load_type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Ref_phone_type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Ref_process_type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Ref_region',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=511)),
            ],
        ),
        migrations.CreateModel(
            name='Payments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField()),
                ('created', models.DateField(auto_now_add=True)),
                ('agreement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Agreement')),
            ],
        ),
        migrations.CreateModel(
            name='Loader',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_name', models.CharField(max_length=100)),
                ('items_loaded', models.IntegerField(default=0)),
                ('items_rejected', models.IntegerField(default=0)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Ref_load_status')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Ref_load_type')),
            ],
        ),
        migrations.CreateModel(
            name='Ispol_sheet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateField(auto_now_add=True)),
                ('agreement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Agreement')),
                ('nadpis', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Ispol_nadpis')),
            ],
        ),
        migrations.CreateModel(
            name='Customer_phone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=15)),
                ('deactivated', models.CharField(default='N', max_length=1)),
                ('created', models.DateField(auto_now_add=True)),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Ref_phone_type')),
            ],
        ),
        migrations.CreateModel(
            name='Customer_address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('addr', models.CharField(max_length=511)),
                ('index', models.IntegerField(null=True)),
                ('deactivated', models.CharField(default='N', max_length=1)),
                ('created', models.DateField(auto_now_add=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fk_address_customer_id', to='api.Customer')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fk_ref_address_type_id', to='api.Ref_address_type')),
            ],
        ),
        migrations.AddField(
            model_name='agreement',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fk_agreement_customer_id', to='api.Customer'),
        ),
        migrations.AddField(
            model_name='agreement',
            name='loader',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Loader'),
        ),
    ]

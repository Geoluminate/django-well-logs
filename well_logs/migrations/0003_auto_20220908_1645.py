# Generated by Django 3.2.15 on 2022-09-08 14:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('well_logs', '0002_alter_operator_table'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='data',
            table='well_logs_data',
        ),
        migrations.AlterModelTable(
            name='log',
            table='well_logs_log',
        ),
        migrations.AlterModelTable(
            name='well',
            table='well_logs_well',
        ),
    ]

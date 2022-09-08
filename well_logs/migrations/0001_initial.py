# Generated by Django 3.2.15 on 2022-09-08 14:30

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Operator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Well',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.PositiveSmallIntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1900), django.core.validators.MaxValueValidator(2050)], verbose_name='year')),
                ('comment', models.TextField(blank=True, null=True, verbose_name='comments')),
                ('added', models.DateTimeField(auto_now_add=True, verbose_name='date added')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='last modified')),
                ('operator', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='logs', to='well_logs.operator', verbose_name='well')),
                ('well', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='logs', to='well_logs.well', verbose_name='well')),
            ],
        ),
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.FloatField(verbose_name='value')),
                ('uncertainty', models.FloatField(blank=True, null=True, verbose_name='uncertainty')),
                ('depth', models.FloatField(verbose_name='depth (m)')),
                ('log', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='data', to='well_logs.log', verbose_name='log')),
            ],
            options={
                'ordering': ['depth'],
                'unique_together': {('value', 'depth', 'log')},
            },
        ),
    ]

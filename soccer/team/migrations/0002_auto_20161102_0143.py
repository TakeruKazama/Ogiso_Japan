# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-01 16:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match',
            name='draw',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='draw', to='team.Team'),
        ),
        migrations.AlterField(
            model_name='match',
            name='loser',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='lose', to='team.Team'),
        ),
        migrations.AlterField(
            model_name='match',
            name='winner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='win', to='team.Team'),
        ),
    ]

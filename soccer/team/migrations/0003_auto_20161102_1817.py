# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-02 09:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0002_auto_20161102_0143'),
    ]

    operations = [
        migrations.AddField(
            model_name='match',
            name='draw_score',
            field=models.IntegerField(default=0, verbose_name='引き分け時の点数'),
        ),
        migrations.AddField(
            model_name='match',
            name='looser_score',
            field=models.IntegerField(default=0, verbose_name='敗者者の点数'),
        ),
        migrations.AddField(
            model_name='match',
            name='winner_score',
            field=models.IntegerField(default=0, verbose_name='勝者の点数'),
        ),
        migrations.AlterField(
            model_name='match',
            name='draw',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='draw', to='team.Team'),
        ),
        migrations.AlterField(
            model_name='match',
            name='loser',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='lose', to='team.Team'),
        ),
        migrations.AlterField(
            model_name='match',
            name='winner',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='win', to='team.Team'),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Computational_Chemistry',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('maths_heavy', models.CharField(max_length=10)),
                ('time_to_be_competent', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Science',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('topic', models.CharField(max_length=200)),
                ('lab_involvment', models.CharField(max_length=200)),
                ('popularity', models.CharField(max_length=100)),
                ('picture', models.CharField(max_length=10000)),
            ],
        ),
        migrations.AddField(
            model_name='computational_chemistry',
            name='subtopic',
            field=models.ForeignKey(to='ScienceBlog.Science'),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ScienceBlog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='subfield',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('maths_heavy', models.CharField(max_length=10)),
                ('time_to_be_competent', models.CharField(max_length=250)),
                ('subtopic', models.ForeignKey(to='ScienceBlog.Science')),
            ],
        ),
        migrations.RemoveField(
            model_name='computational_chemistry',
            name='subtopic',
        ),
        migrations.DeleteModel(
            name='Computational_Chemistry',
        ),
    ]

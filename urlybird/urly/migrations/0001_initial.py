# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Bookmark',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('title', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('longurl', models.URLField()),
                ('shorturl', models.CharField(max_length=8)),
                ('time_created', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='urly')),
            ],
        ),
        migrations.CreateModel(
            name='Click',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('bookmark', models.ForeignKey(to='urly.Bookmark')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

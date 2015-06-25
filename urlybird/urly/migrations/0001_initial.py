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
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('longurl', models.URLField()),
                ('shorturl', models.CharField(max_length=8)),
                ('time_created', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(related_name='urly', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Click',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('bookmark', models.ForeignKey(to='urly.Bookmark')),
                ('user', models.ForeignKey(related_name='clicks', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

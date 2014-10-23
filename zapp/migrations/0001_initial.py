# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('user', models.OneToOneField(serialize=False, primary_key=True, to=settings.AUTH_USER_MODEL)),
                ('zoobars', models.IntegerField(default=10)),
                ('profile', models.TextField(max_length=5000, default='')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Transfer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('amount', models.IntegerField()),
                ('time', models.DateTimeField(auto_now=True)),
                ('recipient', models.ForeignKey(to='zapp.Person', related_name='received_transfers')),
                ('sender', models.ForeignKey(to='zapp.Person', related_name='sent_transfers')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]

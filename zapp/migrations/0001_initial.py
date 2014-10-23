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
            name='Person',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('zoobars', models.IntegerField(default=10)),
                ('profile', models.TextField(max_length=5000, default='')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Transfer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('amount', models.IntegerField()),
                ('time', models.DateTimeField()),
                ('recipient', models.ForeignKey(related_name='received_transfers', to='zapp.Person')),
                ('sender', models.ForeignKey(related_name='sent_transfers', to='zapp.Person')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]

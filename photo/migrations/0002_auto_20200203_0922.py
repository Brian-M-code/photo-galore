# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-02-03 06:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('photo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Description',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_description', models.CharField(max_length=30)),
                ('editor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='photo.Editor')),
            ],
        ),
        migrations.RemoveField(
            model_name='image',
            name='image_description',
        ),
        migrations.AddField(
            model_name='image',
            name='image_description',
            field=models.ManyToManyField(to='photo.Description'),
        ),
    ]
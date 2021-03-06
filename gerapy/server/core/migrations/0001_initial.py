# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-10-17 18:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=None, max_length=255)),
                ('ip', models.GenericIPAddressField(null=True)),
                ('port', models.IntegerField(blank=True, default=6800, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Deploy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(blank=True, max_length=255, null=True)),
                ('deployed_at', models.DateTimeField(blank=True, default=None, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Client')),
            ],
        ),
        migrations.CreateModel(
            name='Monitor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=None, max_length=255)),
                ('description', models.CharField(blank=True, default='', max_length=255)),
                ('type', models.CharField(blank=True, default='', max_length=255)),
                ('configuration', models.TextField(blank=True, default='')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=None, max_length=255)),
                ('description', models.CharField(blank=True, max_length=255, null=True)),
                ('egg', models.CharField(blank=True, max_length=255, null=True)),
                ('configuration', models.TextField(blank=True, null=True)),
                ('configurable', models.IntegerField(blank=True, default=0)),
                ('built_at', models.DateTimeField(blank=True, default=None, null=True)),
                ('generated_at', models.DateTimeField(blank=True, default=None, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('clients', models.ManyToManyField(through='core.Deploy', to='core.Client')),
            ],
        ),
        migrations.AddField(
            model_name='monitor',
            name='project',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Project'),
        ),
        migrations.AddField(
            model_name='deploy',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Project'),
        ),
        migrations.AlterUniqueTogether(
            name='deploy',
            unique_together=set([('client', 'project')]),
        ),
    ]
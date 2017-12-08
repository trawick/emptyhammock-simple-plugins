# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2017-12-08 14:21
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import djangocms_text_ckeditor.fields
import filer.fields.image


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.FILER_IMAGE_MODEL),
        ('cms', '0016_auto_20160608_1535'),
        ('simple_plugins', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SimplePageTeaserPluginModel',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='simple_plugins_simplepageteaserpluginmodel', serialize=False, to='cms.CMSPlugin')),
                ('flavor', models.PositiveSmallIntegerField(choices=[(1, 'Bold headings and action button'), (2, 'Photo and read-more button'), (3, 'Simple'), (4, 'More stories link')])),
                ('override_title', models.CharField(blank=True, max_length=80)),
                ('subtitle', models.CharField(blank=True, max_length=80)),
                ('content', djangocms_text_ckeditor.fields.HTMLField(blank=True)),
                ('image', filer.fields.image.FilerImageField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.FILER_IMAGE_MODEL)),
                ('page', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='cms.Page')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.AlterField(
            model_name='simpletextpluginmodel',
            name='flavor',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Not yet implemented')]),
        ),
        migrations.AlterField(
            model_name='textandimagepluginmodel',
            name='flavor',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Not yet implemented')]),
        ),
    ]

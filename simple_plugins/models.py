from cms.models import CMSPlugin
from django.conf import settings
from django.db import models
from djangocms_text_ckeditor.fields import HTMLField
from django.utils.functional import lazy
from filer.fields.image import FilerImageField


def _get_choices(plugin_nickname):
    choices = settings.SIMPLE_CONTENT_SETTINGS[plugin_nickname]['choices']
    return [
        (choice['flavor'], choice['description'])
        for choice in choices
    ]


def get_text_and_image_choices():
    return _get_choices('SimpleTextAndImage')


def get_text_choices():
    return _get_choices('SimpleText')


class TextAndImagePluginModel(CMSPlugin):
    flavor = models.PositiveSmallIntegerField(blank=False, choices=lazy(get_text_and_image_choices, list)())
    title = models.CharField(max_length=80, blank=False)
    subtitle = models.CharField(max_length=80, blank=True)
    content = HTMLField(blank=False)
    image = FilerImageField(null=False, blank=False)

    def __str__(self):
        return self.title


class SimpleTextPluginModel(CMSPlugin):
    flavor = models.PositiveSmallIntegerField(blank=False, choices=lazy(get_text_choices, list)())
    title = models.CharField(max_length=80, blank=False)
    subtitle = models.CharField(max_length=80, blank=True)
    content = HTMLField(blank=False)

    def __str__(self):
        return self.title

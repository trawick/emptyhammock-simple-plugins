from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.conf import settings

from . import models


def get_template_file(plugin_nickname, flavor):
    choices = settings.SIMPLE_CONTENT_SETTINGS[plugin_nickname]['choices']
    for choice in choices:
        if choice['flavor'] == flavor:
            return choice['template']


@plugin_pool.register_plugin
class SimpleTextAndImagePlugin(CMSPluginBase):
    model = models.TextAndImagePluginModel
    cache = False

    def get_render_template(self, context, instance, placeholder):
        return get_template_file('SimpleTextAndImage', instance.flavor)


@plugin_pool.register_plugin
class SimpleTextPlugin(CMSPluginBase):
    model = models.SimpleTextPluginModel
    cache = False

    def get_render_template(self, context, instance, placeholder):
        return get_template_file('SimpleText', instance.flavor)
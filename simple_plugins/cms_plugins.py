from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.conf import settings

from . import forms, models


def get_template_file(plugin_nickname, flavor):
    choices = settings.SIMPLE_CONTENT_SETTINGS[plugin_nickname]['choices']
    for choice in choices:
        if choice['flavor'] == flavor:
            return choice['template']


@plugin_pool.register_plugin
class SimplePageTeaserPlugin(CMSPluginBase):
    model = models.SimplePageTeaserPluginModel
    form = forms.SimplePageTeaserForm
    cache = False

    def get_render_template(self, context, instance, placeholder):
        return get_template_file('SimplePageTeaser', instance.flavor)


@plugin_pool.register_plugin
class SimpleURLTeaserPlugin(CMSPluginBase):
    model = models.SimpleURLTeaserPluginModel
    form = forms.SimpleURLTeaserForm
    cache = False

    def get_render_template(self, context, instance, placeholder):
        return get_template_file('SimpleURLTeaser', instance.flavor)


@plugin_pool.register_plugin
class SimpleTextAndImagePlugin(CMSPluginBase):
    model = models.TextAndImagePluginModel
    form = forms.SimpleTextAndImageForm
    cache = False

    def get_render_template(self, context, instance, placeholder):
        return get_template_file('SimpleTextAndImage', instance.flavor)


@plugin_pool.register_plugin
class SimpleImagePlugin(CMSPluginBase):
    model = models.SimpleImagePluginModel
    form = forms.SimpleImageForm
    cache = False

    def get_render_template(self, context, instance, placeholder):
        return get_template_file('SimpleImage', instance.flavor)


@plugin_pool.register_plugin
class SimpleTextPlugin(CMSPluginBase):
    model = models.SimpleTextPluginModel
    form = forms.SimpleTextForm
    cache = False

    def get_render_template(self, context, instance, placeholder):
        return get_template_file('SimpleText', instance.flavor)

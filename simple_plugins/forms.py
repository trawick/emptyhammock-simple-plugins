from cms.models import Page
from dal import autocomplete
from django import forms
from django.forms.models import ModelForm


class DynamicFlavorChoicesMixin(object):

    def setup_flavor_choices(self):
        choices = self.Meta.model.get_flavor_choices_fun()()
        self.fields['flavor'].choices = choices
        self.fields['flavor'].widget = forms.Select(choices=choices)


class SimplePageTeaserForm(DynamicFlavorChoicesMixin, ModelForm):

    page = forms.ModelChoiceField(
        queryset=Page.objects.drafts(),
        widget=autocomplete.ModelSelect2(
            url='simple_plugins:page-autocomplete',
            # XXX not working!
            attrs={
                'data-placeholder': 'Start typing the page title to search...'
            },
        )
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setup_flavor_choices()


class SimpleURLTeaserForm(DynamicFlavorChoicesMixin, ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setup_flavor_choices()


class SimpleTextAndImageForm(DynamicFlavorChoicesMixin, ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setup_flavor_choices()


class SimpleTextForm(DynamicFlavorChoicesMixin, ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setup_flavor_choices()

from cms.models import Page
from django.forms.models import ModelForm


class SimplePageTeaserForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['page'].queryset = Page.objects.drafts()

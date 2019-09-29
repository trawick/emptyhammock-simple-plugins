from django.conf.urls import url

from . import autocomplete_views as autocomplete

app_name = 'simple_plugins'

urlpatterns = [
    url(
        r'^page-autocomplete/$',
        autocomplete.PageAutocomplete.as_view(),
        name='page-autocomplete',
    ),
]

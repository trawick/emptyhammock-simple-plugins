from django.urls import path

from . import autocomplete_views as autocomplete

app_name = 'simple_plugins'

urlpatterns = [
    path(
        'page-autocomplete/',
        autocomplete.PageAutocomplete.as_view(),
        name='page-autocomplete',
    ),
]

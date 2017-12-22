# Changes and migration requirements

## Version 0.0.3

### Requirements and URL changes

You must now include `django-autocomplete-lite` and its dependencies, in
support of autocompletion for some CMS plugins.  `dal` and `dal_select2`
need to be added to `INSTALLED_APPS` before `django.contrib.admin`.

Your top-level `urls.py` should include new URL definitions for this app:

```
    url(r'^simple_plugins/', include('simple_plugins.urls', namespace='simple_plugins')),
```

### SimpleTextPlugin and TextAndImagePlugin changes

These no longer require `title` to be set, possibly affecting templates.

## Version 0.0.2

### Simple Page Teaser plugin added

You must now declare `SIMPLE_CONTENT_SETTINGS['SimplePageTeaser']` to
define flavor choices.

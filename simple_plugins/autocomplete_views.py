from cms.models import Page
from dal import autocomplete


class PageAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        if not self.request.user.is_staff:
            return Page.objects.none()

        qs = Page.objects.drafts()
        if self.q:
            qs = qs.filter(title_set__title__icontains=self.q)

        return qs

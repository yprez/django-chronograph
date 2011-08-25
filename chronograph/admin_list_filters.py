from django.utils.translation import ugettext_lazy as _
from django.contrib.admin import SimpleListFilter

class JobErrorsOnlyFilter(SimpleListFilter):
    # Human-readable title which will be displayed in the
    # right admin sidebar just above the filter options.
    title = _('Jobs With Errors')

    # Parameter for the filter that will be used in the URL query.
  #  parameter_name = 'decade'

    def lookups(self, request, model_admin):
        """
        Returns a list of tuples. The first element in each
        tuple is the coded value for the option that will
        appear in the URL query. The second element is the
        human-readable name for the option that will appear
        in the right sidebar.
        """
        return (
            ('Stderr', _('Bad Jobs')),
        )

    def queryset(self, request, queryset):
        """
        Returns the filtered queryset based on the value
        provided in the query string and retrievable via
        `self.value()`.
        """
        # Compare the requested value ('stderr')
        # to decide how to filter the queryset.
        if self.value() == 'stderr':
            return queryset.filter(stderr__isnull=False)
        
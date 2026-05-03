from django.views.generic.base import ContextMixin
from directory.models import (
    Category,
    Featured,
)

# Provides List of Featured Businesses to Views
class FooterContextMixin(ContextMixin):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['featured_business_list'] = [ feature.business for feature in Featured.objects.all() ]
        context['category_list'] = Category.objects.all()
        return context
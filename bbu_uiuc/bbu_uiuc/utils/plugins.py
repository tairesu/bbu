from django.views.generic.base import ContextMixin
from directory.models import (
    Category,
    Featured,
)


# Provides List of Categories to Views
class CategoryContextMixin(ContextMixin):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category_list'] = Category.objects.all()
        return context

# Provides List of Featured Businesses to Views
class FeaturedBusinessListContextMixin(ContextMixin):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['featured_business_list'] = Featured.objects.all()
        return context
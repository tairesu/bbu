from django.shortcuts import render
from django.views.generic import (
    TemplateView,
)
from bbu_uiuc.utils.plugins import (
    CategoryContextMixin,
    FeaturedBusinessListContextMixin
)


class LandingPageView(TemplateView, FeaturedBusinessListContextMixin, CategoryContextMixin):
    template_name = 'home.html'


class AboutView(TemplateView, FeaturedBusinessListContextMixin, CategoryContextMixin):
    template_name = 'about.html'

from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import (
    TemplateView,
    CreateView

)
from directory.forms import (
    NewBusinessForm
)
from bbu_uiuc.utils.plugins import (
    CategoryContextMixin,
    FeaturedBusinessListContextMixin
)
from directory.models import Business


class LandingPageView(TemplateView, FeaturedBusinessListContextMixin, CategoryContextMixin):
    template_name = 'home.html'


class AboutView(TemplateView, FeaturedBusinessListContextMixin, CategoryContextMixin):
    template_name = 'about.html'


class BusinessCreateView(CreateView, FeaturedBusinessListContextMixin, CategoryContextMixin):
    template_name = 'business_create.html'
    form_class = NewBusinessForm
    model = Business 
    success_url = reverse_lazy('home_urlpattern')  

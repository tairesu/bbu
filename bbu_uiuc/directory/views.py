from django.shortcuts import render, redirect
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

    def get(self, request, *args, **kwargs):
        form = NewBusinessForm()
        return super().get(request, kwargs)
        
    
    def post(self, request, *args, **kwargs):
        form = NewBusinessForm(request.POST)
        print(f"Welcome to the Business Create Space. \n ")
        print(f"Args Passed: {args}\n")
        print(f"Args Passed: {kwargs}\n")
        



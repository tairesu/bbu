from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import (
    TemplateView,
    CreateView,
    DetailView,

)
from directory.forms import (
    NewBusinessForm
)
from bbu_uiuc.utils.plugins import (
    FooterContextMixin,
)
from directory.models import Business


class LandingPageView(TemplateView, FooterContextMixin):
    template_name = 'home.html'


class AboutView(TemplateView, FooterContextMixin):
    template_name = 'about.html'


class BusinessCreateView(CreateView, FooterContextMixin):
    template_name = 'business_create.html'
    form_class = NewBusinessForm
    model = Business 
    success_url = reverse_lazy('home_urlpattern')  

class BusinessDetailView(DetailView, FooterContextMixin):
    model = Business
    template_name = 'business_detail.html'

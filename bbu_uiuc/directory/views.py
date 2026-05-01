from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import (
    TemplateView,
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


class BusinessCreateView(TemplateView, FeaturedBusinessListContextMixin, CategoryContextMixin):
    template_name = 'business_create.html'
    active_form = 'new_business_first_form.html'

    def check_fields(self, post_data)-> tuple:
        if 'name' in post_data.keys() and 'description' in post_data.keys():
            print(f"First Form Post:{post_data} \n")
            # The name and description fields of the first form are required
            if len(post_data['name']) < 2 or len(post_data['description']) < 10:
                return (False, "Name and Description Fields are required")
            # The name must be unique
            if Business.objects.filter(name=post_data['name']).exists():
                return (False, "Name Already Exists")
        elif 'email' in post_data.keys():
            print(f"Second Form: {post_data} \n")
        return (True, "OK")
    
    def get_context_data(self, **kwargs):
        print("Looks Like we have these kwargs at get_context_data" , kwargs)
        context_data = super().get_context_data(**kwargs)
        context_data['active_form'] = self.active_form
        return context_data
    
    def update_context_data(self,data_dict, **kwargs):
        context_data = self.get_context_data(**kwargs)
        context_data.update(data_dict)
        return context_data
       
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.get_context_data(**kwargs))
    
    def post(self, request, *args, **kwargs):
        print(f"Welcome to the Business Create Space. \n ")
        print(f"Args Passed: {args}\n")
        print(f"Args Passed: {kwargs}\n")
        form_success, msg = self.check_fields(request.POST)
        if not form_success:
            return render(request, self.template_name, self.update_context_data({'given_name': request.POST.get('name'), 'given_desciption': request.POST.get('description'), 'form_errors': msg}))
        #Go on to form 2
        return self.move_to_next_form(request, request.POST)

    def move_to_next_form(self, request, post_data):
        print("Move_to_next_form Post_data Keys: ", post_data.keys())
        if 'name' in post_data.keys():
            self.active_form = 'new_business_second_form.html'
        elif 'email' in post_data.keys():
            self.active_form = 'new_business_third_form.html'
        return render(request, self.template_name, self.get_context_data())
        




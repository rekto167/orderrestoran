from django.shortcuts import render
from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'homepage.html'

    def get_context_data(self, *args, **kwargs):
        context = {
            'page_title': 'Homepage'
        }
        return context


class AboutView(TemplateView):
    template_name = 'about.html'

    def get_context_data(self, *args, **kwargs):
        context = {
            'page_title': 'About'
        }
        return context

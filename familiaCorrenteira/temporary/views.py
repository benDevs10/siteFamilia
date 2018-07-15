from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.views.generic import TemplateView

def home_page(request):
    template_name = 'home.html'
    content = {}

    return render(request, template_name, content)

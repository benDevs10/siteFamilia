from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.views.generic import TemplateView
from temporary.models import Corrente
from random import randint

def home_page(request):
    template_name = 'home.html'
    query_list = Corrente.objects.filter(disponivel=True)
    choice = query_list[randint(0, len(query_list)-1)]

    content = {
        'corrente': choice,
    }

    return render(request, template_name, content)

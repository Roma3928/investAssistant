from django.shortcuts import render
from django.views.generic import ListView
from news.models import News
from .models import *


class IndexView(ListView):
    model = News
    ordering = ["id"]
    template_name = "index.html"
    context_object_name = 'news'


class TaxView(ListView):
    model = Tax
    ordering = ["state"]
    template_name = "core/tax.html"
    context_object_name = 'tax'


def analytics(request):
    return render(request, 'core/analytics.html')

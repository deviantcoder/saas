from django.shortcuts import render
from django.http import HttpResponse

from visits.models import PageVisit


def home_view(request, *args, **kwargs):
    return about_view(request, *args, **kwargs)


def about_view(request, *args, **kwargs):
    qs = PageVisit.objects.all()
    page_qs = PageVisit.objects.filter(path=request.path)

    try:
        percent = (page_qs.count() * 100.0) / qs.count()
    except ZeroDivisionError:
        percent = 0
    
    my_title = 'My Page'
    my_context = {
        'page_title': my_title,
        'page_visit_count': page_qs.count(),
        'total_visit_count': qs.count(),
        'percent': percent
    }
    html_template = 'home.html'

    PageVisit.objects.create(path=request.path)

    return render(request, html_template, my_context)
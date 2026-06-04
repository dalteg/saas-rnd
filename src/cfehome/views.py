import pathlib
from django.shortcuts import render
from django.http import HttpResponse
from visits.models import PageVisit

this_dir = pathlib.Path(__file__).resolve().parent

def home_view(requests, *args, **kwargs):
    return about_view(requests,*args, **kwargs)

def about_view(requests, *args, **kwargs):
    qs = PageVisit.objects.all()
    page_qs = PageVisit.objects.filter(path=requests.path)
    try:
         percent=(page_qs.count()*100.0)/qs.count()
    except:
        percent = 0
    my_title = "My Page"
    my_context = {
        "page_title": my_title,
        "page_visit_count": page_qs.count(),
        "percent": percent,
        "total_visit_count":qs.count()
    }

    html_template = "home.html"
    PageVisit.objects.create(path=requests.path)
    return render(requests, html_template, my_context)
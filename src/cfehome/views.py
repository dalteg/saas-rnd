import pathlib
from django.shortcuts import render
from django.http import HttpResponse
from visits.models import PageVisit

this_dir = pathlib.Path(__file__).resolve().parent

def home_page_view(requests, *args, **kwargs):
    qs = PageVisit.objects.all()
    page_qs = PageVisit.objects.filter(path=requests.path)
    my_title = "My Page"
    my_context = {
        "page_title": my_title,
        "page_visit_count": page_qs.count(),
        "percent":(page_qs.count()*100.0)/qs.count(),
        "total_visit_count":qs.count()
    }

    html_template = "home.html"
    PageVisit.objects.create(path=requests.path)
    return render(requests, html_template, my_context)


def about_page_view(requests, *args, **kwargs):
    my_title = "My Page"
    my_context = {
        "page_title": my_title
    }
    html_template = "about.html"
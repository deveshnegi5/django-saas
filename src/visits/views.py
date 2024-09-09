from django.shortcuts import render
from .models import pagevisits

def homepage(request):
    queryset=pagevisits.objects.all()
    page_qs= pagevisits.objects.filter(page=request.path)
    print(request.path)
    print(page_qs.count())
    print(queryset.count())
    try:
        percent=(page_qs.count()*100.0)/queryset.count()
    except:
        percent=0
    context={"title": "Jai shree ram",
             "queryset_count": queryset.count(),
             "percent":percent,
             "queryset": queryset}
    template="home.html"
    pagevisits.objects.create(page=request.path)
    # print(queryset.visit_time)
    return render(request,template,context)

def about(request):
    queryset=pagevisits.objects.all()
    page_qs= pagevisits.objects.filter(page=request.path)
    print(request.path)
    try:
        percent=(page_qs.count()*100.0)/queryset.count()
    except:
        percent=0
    context={"title": "Jai shree ram",
             "queryset_count": queryset.count(),
             "percent":percent,
             "queryset": queryset}
    template="home.html"
    pagevisits.objects.create(page=request.path)
    # print(queryset.visit_time)
    return render(request,template,context)
from django.shortcuts import render
from .models import pagevisits

def homepage(request):
    queryset=pagevisits.objects.all()
    context={"title": "Jai shree ram",
             "queryset_count": queryset.count(),
             "queryset": queryset}
    template="home.html"
    pagevisits.objects.create()
    # print(queryset.visit_time)
    return render(request,template,context)
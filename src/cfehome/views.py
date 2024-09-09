from django.shortcuts import render

def homepage(request):
    context={"title": "Jai shree ram"}
    template="home.html"
    return render(request,template,context)
from django.shortcuts import render

# Create your views here.
def urls(request):
    return render(request,"urls/urls.html")

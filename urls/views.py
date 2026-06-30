from django.shortcuts import render

# Create your views here.
def urls(request):
    return render(request,"urls/urls.html")

def yellow_urls(request):
    return render(request,"urls/yellow_urls.html")


# from django.http import HttpResponse
from django.shortcuts import render


def  homepage(request):
    return render(request, 'home.html')
    # return HttpResponse("Hello World! I'm HOME.")


def  aboutpage(request):
        return render(request, 'about.html')
    # return HttpResponse("My About page is Here.")
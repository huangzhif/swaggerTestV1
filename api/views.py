from django.shortcuts import render


# Create your views here.


def index(request):
    return render(request, 'api/index.html')


def docs(request):
    return render(request, 'api/docs.json')


def module(request, json):
    return render(request, 'api/%s.json' % json)

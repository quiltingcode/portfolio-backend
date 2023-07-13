from django.shortcuts import render

def say_hello(request):
    return HttpResponse('hello')

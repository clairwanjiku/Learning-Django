from django.shortcuts import render # type: ignore
from django.http import HttpResponse # type: ignore

def say_hello(request):
   
    return render(request, 'hello.html',{'name': 'Clair'})

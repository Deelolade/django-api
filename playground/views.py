from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# Django views only take request (not response)

# render() expects:
# render(request, template_name, context)
# But you passed response and no template

def say_hello(request):
    return render(request, 'hello.html', {'name':'Deelolade' } )

def get_user_data (request):
    return render(request, 'user.html', {
        "name": "habeeb",
        "age": 10,
        "address": "lagos"
    })
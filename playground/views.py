from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post

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

def home(request):
    posts = Post.objects.all()
    return render(request, 'home.html', {'posts' : posts})

def post ( request, id):
    # post = Post.objects.get(id = id)
    post = get_object_or_404(Post, id=id)
    return render( request, 'post.html', {'post' : post})
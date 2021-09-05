from django.shortcuts import render
from .models import User, Post

import requests
 
# получение данных из бд
def index(request):
    usersJson = requests.get('http://jsonplaceholder.typicode.com/users').json()
    postsJson = requests.get('http://jsonplaceholder.typicode.com/posts').json()
    for user in usersJson:
        user = User(**user)
        user.save()
    for post in postsJson:
        post = Post(**post)
        post.save()
    return render(request, "index.html", {"users": User.objects.all(), "posts": Post.objects.all()})
 
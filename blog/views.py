from django.shortcuts import render
from .models import Post


def posts(request):
    infos = Post.objects
    return render(request, 'posts.html', {'infos': infos})

from django.shortcuts import render, get_object_or_404
from .models import Post


def posts(request):
    infos = Post.objects
    return render(request, 'posts.html', {'infos': infos})


def specific_post(request, post_id):
    a = 1 if post_id == 'hello' else 2
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'post.html', {'post': post})

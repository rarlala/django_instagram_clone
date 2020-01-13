from django.shortcuts import render

from posts.models import Post


def post_list(request):
    posts = Post.objects.order_by('-pk')
    context = {
        'posts' : posts,
    }

    return render(request, 'posts/post-list.html', context)
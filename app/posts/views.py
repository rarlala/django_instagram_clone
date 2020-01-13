from django.shortcuts import render, redirect

from posts.models import Post, PostLike


def post_list(request):
    posts = Post.objects.order_by('-pk')
    context = {
        'posts': posts,
    }

    return render(request, 'posts/post-list.html', context)


def post_like(request, pk):
    post = Post.objects.get(pk=pk)
    user = request.user

    post_like_qs = PostLike.objects.filter(post=post, user=user)

    print("post_like_qs", post_like_qs)

    if post_like_qs.exists():
        post_like_qs.delete()

    else:
        PostLike.objects.create(post=post, user=user)
    return redirect('posts:post-list')

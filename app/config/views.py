from django.shortcuts import render, redirect


def index(request):
    if request.user.is_authenticated:
        return redirect('posts:post-list')

    else:
        return render(request, 'index.html')
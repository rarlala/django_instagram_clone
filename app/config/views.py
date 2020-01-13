from django.shortcuts import render


def index(request):
    if request.user.is_authenticated:
        return render('posts:post-list')
    return render(request, 'index.html')
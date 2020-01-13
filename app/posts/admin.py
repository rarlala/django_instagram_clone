from django.contrib import admin

from posts.models import Post, PostImage, PostComment, PostLike


@admin.register(Post)
class Post(admin.ModelAdmin):
    pass

@admin.register(PostImage)
class PostImage(admin.ModelAdmin):
    pass

@admin.register(PostComment)
class PostComment(admin.ModelAdmin):
    pass

@admin.register(PostLike)
class PostLike(admin.ModelAdmin):
    pass
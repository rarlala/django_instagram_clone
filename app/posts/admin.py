from django.contrib import admin

from posts.models import Post, PostImage, PostComment, PostLike


class PostImageInline(admin.TabularInline):
    model = PostImage
    extra = 1

class PostCommentInline(admin.TabularInline):
    model = PostComment
    extra = 1

@admin.register(Post)
class Post(admin.ModelAdmin):
    list_display = ('author', 'content', 'created')

class PostAdmin(admin.ModelAdmin):
    list_display = ('author', 'content', 'created')
    list_display_links = ('author', 'content')
    inlines = [
        PostImageInline,
        PostCommentInline,
    ]

@admin.register(PostImage)
class PostImage(admin.ModelAdmin):
    pass

@admin.register(PostComment)
class PostComment(admin.ModelAdmin):
    pass

@admin.register(PostLike)
class PostLike(admin.ModelAdmin):
    pass



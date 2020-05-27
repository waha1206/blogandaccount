from django.contrib import admin
from django.contrib.admin.templatetags.admin_list import admin_list_filter

from .models import Post, Comment


# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        'title', 'slug', 'author', 'publish', 'status'
    )
    list_filter = ('status', 'created', 'publish', 'author')
    search_fields = ('title', 'slug')
    prepopulated_fields = {'slug': ('title',)}
    raw_id_files = ('author')
    date_hierarchy = 'publish'
    ordering = ('status', 'publish')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'created', 'post', 'active')
    list_filter = ('active', 'created', 'email')
    search_fields = ('username', 'email')

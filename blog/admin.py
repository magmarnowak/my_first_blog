from django.contrib import admin
from .models import Post, Comment

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published_date')
    list_filter = ('created_date', 'published_date', 'author')
    search_fields = ('title', 'text')
    raw_id_fields = ('author',)
    date_hierarchy = 'published_date'
    ordering = ['published_date']

class CommentAdmin(admin.ModelAdmin):
    list_display = ('text', 'author', 'created_date', 'post', 'approved_comment')
    list_filter = ('author', 'created_date', 'post', 'approved_comment')
    search_fields = ('post', 'author')
    date_hierarchy = 'created_date'
    ordering = ['created_date']

admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)

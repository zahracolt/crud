from django.contrib import admin
from django.contrib import admin
from .models import Article, Comment # new

# Register your models here.
class CommentInline(admin.StackedInline): # new
    model = Comment
class ArticleAdmin(admin.ModelAdmin): # new
    inlines = [
CommentInline,
]

admin.site.register(Article)
admin.site.register(Comment)
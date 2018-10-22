from django.contrib import admin
from .models import Category, Tag, Article, Like
from django.db import models
from django.forms import Textarea


# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)


class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_time', 'modified_time', 'author', 'category')
    formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows': 30, 'cols': 120})}
    }


class LikeAdmin(admin.ModelAdmin):
    list_display = ('ip', 'article')


admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Like, LikeAdmin)
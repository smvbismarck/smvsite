from django.contrib import admin
from .models import Article, Image


class ImageInline(admin.StackedInline):
    model = Image
    extra = 0


class ArticleAdmin(admin.ModelAdmin):
    inlines = [ImageInline]


admin.site.register(Article, ArticleAdmin)
# Register your models here.

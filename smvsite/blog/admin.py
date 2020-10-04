from django.contrib import admin, messages
from django.utils.translation import ngettext
from .models import Article, Image


class ImageInline(admin.StackedInline):
    model = Image
    extra = 0


def make_blogpost(self, request, queryset):
    updated = queryset.update(blogpost=True)
    self.message_user(request, ngettext(
        '%d blogpost was successfully converted into a komitee.',
        '%d blogposts were successfully converted into komitees.',
        updated,
    ) % updated, messages.SUCCESS)


make_blogpost.short_description = "Convert selected articles into a blogpost"


def make_komitee(self, request, queryset):
    updated = queryset.update(blogpost=False)
    self.message_user(request, ngettext(
            '%d komitee was successfully converted into an article.',
            '%d komitees were successfully converted into articles.',
            updated,
        ) % updated, messages.SUCCESS)


make_komitee.short_description = "Convert selected articles into a komitee"


class ArticleAdmin(admin.ModelAdmin):
    inlines = [ImageInline]
    list_display = ["title", "time", "author", "blogpost"]
    list_filter = ["blogpost"]
    search_fields = ["title"]
    actions = [make_blogpost, make_komitee]


admin.site.register(Article, ArticleAdmin)
# Register your models here.

from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from . import models

@admin.register(models.Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['title', 'display_category', 'publish']
    list_editable = ('publish',)
    list_filter = ('publish', 'category',)
    search_fields = ('title',)
    models.Blog.display_category.short_description = _('Categories')
    prepopulated_fields = {'slug': ('title',)}

@admin.register(models.Videocast)
class VideoAdmin(admin.ModelAdmin):
    list_display = ['title', 'display_category', 'publish']
    list_editable = ('publish',)
    list_filter = ('publish', 'category',)
    search_fields = ('title',)
    models.Videocast.display_category.short_description = _('Categories')
    prepopulated_fields = {'slug': ('title',)}

@admin.register(models.Podcast)
class PodcastAdmin(admin.ModelAdmin):
    list_display = ['title', 'display_category', 'publish']
    list_editable = ('publish',)
    list_filter = ('publish', 'category',)
    search_fields = ('title',)
    models.Podcast.display_category.short_description = _('Categories')
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(models.BlogCategory)
admin.site.register(models.VideocastCategory)
admin.site.register(models.PodcastCategory)
admin.site.register(models.Skill)

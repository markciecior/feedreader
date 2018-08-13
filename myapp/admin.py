from django.contrib import admin

# Register your models here.

from .models import Feed, Link

class LinkAdmin(admin.ModelAdmin):
  list_display = ('parentFeed', 'linkId')

class LinkInline(admin.TabularInline):
  model = Link

class FeedAdmin(admin.ModelAdmin):
  list_display = ('description', 'active', 'linkFile')
  inlines = [LinkInline]

admin.site.register(Feed, FeedAdmin)
admin.site.register(Link, LinkAdmin)
from django.contrib import admin
from django.db import models
from .models import Article,Comment

#admin.site.register(Article)
@admin.register(Article) # This is a decorator
class ArticleAdmin(admin.ModelAdmin):
    list_display = ["Title","Author","createdDate"]
    list_display_links = ["Title","createdDate"]
    search_fields = ["Title"]
    list_filter = ["createdDate","Author"]
    class Meta: # We HAVE TO say (Meta)
        model = Article # Here we connected AdminArticle Class and Article class.

admin.site.register(Comment)
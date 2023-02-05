from django.contrib import admin
from django.urls import path
from . import views 

app_name = "article"

urlpatterns = [
    path("",views.articles, name = "articles"),
    path("myarts/",views.myarts, name = "myarts"),
    path("addarticle/",views.addArticle, name = "addarticle"),
    path("article/<int:id>",views.detail,name = "detail"),
    path("edit/<int:id>",views.updateArticle,name = "updateArticle"),
    path("delete/<int:id>",views.deleteArticle,name = "deleteArticle"),
    path("comment/<int:id>",views.addComment,name="comment")
]
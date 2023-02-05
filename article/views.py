import article
from article.models import Article, Comment
from django.shortcuts import get_object_or_404, redirect,render,HttpResponse
from django.urls import reverse
from .forms import ArticleForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Our all forms in HTML files have to contains csrf token

def index(request):
    return render(request,"index.html")

def about(request):
    return render(request,"about.html")

def articles(request):
    keyword = request.GET.get("keyword")
    if keyword:
        articles = Article.objects.filter(Title__contains = keyword)
        return render(request,"articles.html",{"articles" : articles})
    articles = Article.objects.all()
    return render(request,"articles.html",{"articles" : articles}) # We have to return this dictionary for see all articles.

@login_required(redirect_field_name = "Please LogIn", login_url = "login")
def myarts(request):
    articles = Article.objects.filter(Author = request.user)
    return render(request,"myarts.html",{"articles":articles})

@login_required(redirect_field_name = "Please LogIn", login_url = "login")
def addArticle(request):
    form = ArticleForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        article = form.save(commit=False)
        article.Author = request.user
        article.save()
        messages.success(request,"Congrats")
        return redirect("index")
    return render(request,"addarticle.html",{"form" : form})

@login_required(redirect_field_name = "Please LogIn", login_url = "login")
def detail(request,id):
    ###article = Article.objects.filter(id = id).first()
    article = get_object_or_404(Article,id=id)
    comments = article.comments.all()
    return render(request,"detail.html",{"article":article,"comments":comments})

@login_required(redirect_field_name = "Please LogIn", login_url = "login")
def updateArticle(request,id):
    article = get_object_or_404(Article,id = id)
    form = ArticleForm(request.POST or None, request.FILES or None, instance = article) # Like we said instance = article this means form takes the article object that we send it above.
    if form.is_valid():
        article = form.save(commit=False)
        article.Author = request.user
        article.save()
        messages.success(request,"Congrats")
        return redirect("index")
    return render(request,"update.html",{"form" : form})

@login_required(redirect_field_name = "Please LogIn", login_url = "login")
def deleteArticle(request,id):
    article = get_object_or_404(Article,id = id)
    if article.Author.id == request.user.id:
        article.delete()
        messages.success(request,"Congrats You deleted the article")
        return redirect("article:myarts")
    else:
        messages.warning(request," This article not yours... ")
        return redirect("article:myarts")

@login_required(redirect_field_name = "Please LogIn", login_url = "login")
def addComment(request,id):
    article = get_object_or_404(Article,id = id)
    if request.method == "POST":
        comment_author = request.POST.get("comment_author")
        comment_content = request.POST.get("comment_content")
        newComment = Comment(comment_author = comment_author, comment_content = comment_content)
        newComment.article = article
        newComment.save()
    return redirect(reverse("article:detail",kwargs = {"id":id}))
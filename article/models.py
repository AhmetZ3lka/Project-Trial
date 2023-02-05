from django.db import models
from ckeditor.fields import RichTextField

class Article(models.Model):
    Author = models.ForeignKey("auth.User",on_delete=models.CASCADE)
    Title = models.CharField(max_length=50)
    Content = RichTextField()
    createdDate = models.DateTimeField(auto_now_add=True)
    article_image = models.FileField(blank = True, null = True)
    def __str__(self):
        return self.Title
    class Meta:
        ordering = ['-createdDate']

class Comment(models.Model):
    article = models.ForeignKey(Article,on_delete=models.CASCADE,verbose_name="Comment",related_name="comments")
    comment_author = models.CharField(max_length=50)
    comment_content = models.CharField(max_length=300)
    comment_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.comment_content

    class Meta:
        ordering = ['-comment_date']
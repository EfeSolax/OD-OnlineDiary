from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class BlogModel(models.Model):
    author = models.ForeignKey("auth.User", on_delete = models.CASCADE, verbose_name = "Yazar")
    title = models.CharField(max_length = 100, verbose_name = "Başlık")
    content = RichTextField(verbose_name = "İçerik")
    created_at = models.DateTimeField(verbose_name = "Oluşturulma Tarihi", auto_now_add= True)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ["-created_at"]

class CommentModel(models.Model):
    article = models.ForeignKey(BlogModel, on_delete = models.CASCADE, verbose_name= "Günlük", related_name= "comments")
    comment_author = models.CharField(max_length=50, verbose_name= "İsim")
    comment_content = models.CharField(max_length=250, verbose_name= "Yorum")
    comment_date = models.DateField(auto_now_add=True, verbose_name= "Oluşturulma Tarihi")

    def __str__(self):
        return self.comment_content
    
    class Meta:
        ordering = ["-comment_date"]

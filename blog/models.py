from django.db import models
from django.contrib.auth.models import User
from django.db.models import Count


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=70)
    body = models.TextField()
    created_time = models.DateTimeField()
    modified_time = models.DateTimeField()
    excerpt = models.CharField(max_length=200, blank=True)
    author = models.ForeignKey(User)
    category = models.ForeignKey(Category)
    tags = models.ManyToManyField(Tag, blank=True)

    def get_likes(self):
        return Like.objects.filter(article=self).count()

    def __str__(self):
        return self.title


class Like(models.Model):
    ip = models.CharField(max_length=20)
    article = models.ForeignKey(Article)

    def __str__(self):
        return self.ip+'_like_'+self.article.title

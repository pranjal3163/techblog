from django.conf import settings
from django.db import models
from django.utils import timezone
from taggit.managers import TaggableManager
from datetime import datetime
from django.shortcuts import reverse
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    # author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # title = models.CharField(max_length=200)
    # text = models.TextField()
    # slug = models.SlugField(unique=True, max_length=100)
    # tags = TaggableManager()
    # created_date = models.DateTimeField(default=timezone.now)
    # published_date = models.DateTimeField(blank=True, null=True)
    #
    # def publish(self):
    #     self.published_date = timezone.now()
    #     self.save()
    #
    # def __str__(self):
    #     return self.title
    #
    # def filter_by_published_date(self):
    #     return Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')

    title = models.CharField(max_length=100)
    content = models.TextField()
    date = models.DateField(default=datetime.now)
    slug = models.SlugField(unique=True, max_length=100)
    tags = TaggableManager()
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog_post_detail', kwargs={'pk': self.pk})

    def approved_comments(self):
        return self.comments.filter(approved_comment=True)

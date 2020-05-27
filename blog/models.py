from enum import unique

from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils import timezone
from taggit.managers import TaggableManager
from .cn_taggit import CnTaggedItem
from uuslug import slugify


class Post(models.Model):

    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    title = models.CharField(max_length=250)
    # slug = models.CharField(max_length=250, unique_for_date='publish')
    slug = models.SlugField(
        max_length=250, unique_for_date='publish', allow_unicode=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='blog_posts')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(choices=STATUS_CHOICES,
                              max_length=50, default='draft')
    tags = TaggableManager(blank=True, through=CnTaggedItem)

    class Meta:
        ordering = ('-publish', )

        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    def get_url(self):
        # 重定向，建立在class裡面的一個function 他可以傳到templates裡面使用 {{ post.get_url }}
        # 再來要到urls裡面建立一個可以承接他的 path，以這個例子來說如下
        # path('<int:year>/<int:month>/<int:day>/<str:slug>)', views.post_detail, name='post_detail)
        return reverse('blog:post_detail', args=[self.publish.year, self.publish.month, self.publish.day, self.slug])


class Comment(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments')
    username = models.CharField(max_length=120)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return 'Comment by {} on {}'.format(self.username, self.post)

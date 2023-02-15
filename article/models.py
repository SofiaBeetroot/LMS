from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _


class Topic(models.Model):
    TOPIC_TYPES = [
        (1, 'Science'),
        (2, 'News'),
        (3, 'Review'),
        (4, 'Useful knowing'),
        (5, 'Tutorial'),
        (6, 'Best practices')
    ]
    title = models.CharField(max_length=150)
    subtitle = models.CharField(max_length=100, null=True, blank=True)
    text = models.TextField(max_length=10000)
    url = models.URLField(null=True, blank=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    type = models.IntegerField(choices=TOPIC_TYPES)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='author', null=True)


class Comments(models.Model):
    text = models.CharField(max_length=400)
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comment_author')
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name='comment_topic')

    class Meta:
        verbose_name = _("Comments")
        verbose_name_plural = _("Comments")

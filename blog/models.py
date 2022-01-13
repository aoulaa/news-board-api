from django.contrib.auth.models import User
from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=150)
    link = models.URLField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    author_name = models.CharField(max_length=50)  # as a demo it's ChardField

    def __str__(self):
        return self.title


class Upvote(models.Model):
    voter = models.CharField(max_length=50)
    post = models.ForeignKey(Post, related_name="upvote", on_delete=models.CASCADE)

    class Meta:
        unique_together = ("voter", "post")


class Comment(models.Model):
    commenter = models.CharField(max_length=50)  # as a demo it's ChardField
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey("Post", related_name="comments", on_delete=models.CASCADE)

    def __str__(self):
        return self.content

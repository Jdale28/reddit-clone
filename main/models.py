from django.db import models

class Post(models.Model):
    created_at = models.DateTimeField(null=True, blank=True)
    title = models.CharField(max_length=255)
    picture = models.CharField(max_length=400)
    content = models.CharField(max_length=255)
    site_url = models.CharField(max_length=400)
    vote_total = models.IntegerField(null=True, blank=True)
    # user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')

    def __str__(self):
        return self.title


class Comment(models.Model):
    created_at = models.DateTimeField(null=True, blank=True)
    content = models.CharField(max_length=255)
    vote_total = models.IntegerField(null=True, blank=True)
    # user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')

    def __str__(self):
        return self.content
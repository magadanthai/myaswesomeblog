from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateTimeField()
    text = models.CharField(max_length=300)
    image = models.ImageField(upload_to='blog_img')

    def __str__(self):
        return self.title

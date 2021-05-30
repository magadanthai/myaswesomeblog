from django.db import models


class Main(models.Model):
    image = models.ImageField(upload_to='event_img')
    text = models.CharField(max_length=300)

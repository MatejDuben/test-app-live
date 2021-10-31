from django.db import models

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=120)
    body = models.TextField()

    slug = models.SlugField(blank=True, null=True)

    def __str__(self):
        return str(self.title)
from django.db import models
from django.urls import reverse
class Post(models.Model):

    text = models.TextField()
def __str__(self):
    return self.title
def get_absolute_url(self):
    return reverse("post_detail", kwargs={"pk": self.pk})

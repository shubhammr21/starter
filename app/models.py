from django.db import models

# Create your models here.


class TestModel(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse("id")

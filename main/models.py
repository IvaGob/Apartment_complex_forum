from django.db import models

# Create your models here.
class News(models.Model):
    title = models.CharField()
    text = models.TextField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title
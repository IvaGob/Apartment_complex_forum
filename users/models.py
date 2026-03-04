from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    birth_date = models.DateField(null=True,blank=True)
    avatar = models.ImageField(upload_to='avatars/',default='default.png')
    apartment_number = models.CharField(max_length=20)
    description = models.TextField(null=True,blank=True)

    def __str__(self):
        return f"Профіль {self.user.username}"
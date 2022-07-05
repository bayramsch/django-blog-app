from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='profiles', blank=True, default= "avatar.png")
    bio = models.TextField(blank=True)
    
    def __str__(self):
        # return self.user    
        return "{} {}".format(self.user, 'Profile')
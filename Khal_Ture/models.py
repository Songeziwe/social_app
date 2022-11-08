from enum import unique
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.text import slugify

class User(AbstractUser):
  USERNAME_FIELD = "username"
  REQUIRED_FIELDS = []
  status = models.BooleanField(default=False)
  is_staff = models.BooleanField(default=True)
  is_active=models.BooleanField(default=True)
  profile_img = models.ImageField(upload_to="profile/", null=True, blank=True)
  
  def __str__(self):
    return f'{self.first_name} {self.last_name}'

class Post(models.Model):
  timestamp = models.DateField(auto_now_add=True)
  content = models.TextField()
  imageUrl = models.ImageField(upload_to='posts/')
  user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
  slug = models.SlugField()

  def save(self,*args,**kwargs):
    self.slug = slugify(self.user.username)
    return super(Post,self).save(self,*args, **kwargs)

  def __str__(self):
    return f'{self.user} - {self.content}'
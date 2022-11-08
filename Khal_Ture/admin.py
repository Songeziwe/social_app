from django.contrib import admin
from .models import User, Post

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
  list_display = ['first_name', 'last_name', 'email', 'status', 'profile_img']

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['content', 'timestamp', 'user', 'imageUrl']
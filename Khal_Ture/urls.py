from . import views
from django.urls import path

app_name = 'Khal_Ture'

urlpatterns = [
  path('', views.index, name='index'),
  path('login/', views.login, name='login'),
  path('signup/', views.signup, name='signup'),
  path('handleSignIn/', views.handleSignIn, name='handleSignIn'),
  path('handleSignUp/', views.handleSignUp, name='handleSignUp'),
  path('profile/', views.profile, name='profile'),
  path('<slug:slug>/', views.post, name='post-details')
]
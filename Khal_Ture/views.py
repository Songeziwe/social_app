from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login as login_auth, logout
from .models import Post, User

def index(request):
  if request.method == "POST":
    content = request.POST['content']
    file = request.FILES['file']
    post = Post(content=content,imageUrl=file, user=request.user)
    post.save()
    return HttpResponseRedirect(reverse('Khal_Ture:index'))
  users = User.objects.filter(status=True)
  return render(request, 'home.html', { "posts": Post.objects.all(), "onlineUsers": len(users)} )
    

def login(request):
  return render(request, 'login.html')

def signup(request):
  return render(request, 'signup.html')

def profile(request):
  if request.method == 'POST':
    logout(request) 
    return HttpResponseRedirect(reverse('Khal_Ture:index'))

  # TODO: All posts related to the user
  posts = Post.objects.filter(user=request.user)
  # TODO: Pass the posts back
  return render(request, 'profile.html', {"posts": posts})


def post(request, slug):
  post = Post.objects.get(slug=slug)
  print(post)
  return render(request,'post-details.html', {"post": post})

def handleSignIn(request):
  if request.method == 'POST':
    username = request.POST['username'].strip()
    userPassword = request.POST['password'].strip()
    user = authenticate(request, username=username, password=userPassword)
    if user is not None:
      login_auth(request, user)
      # User.objects.filter(username=username)[0].status = True
      user.status = True
      user.save()
      return HttpResponseRedirect(reverse('Khal_Ture:index'))
    else:
      return HttpResponseRedirect(reverse('Khal_Ture:login'))
  else:
    return HttpResponseRedirect(reverse('Khal_Ture:login'))

def handleSignUp(request):
  if request.method == "POST":
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    email = request.POST['email']
    password = request.POST['password']
    profile_pic = request.FILES['profile_pic']
    username = first_name
    user = User(first_name=first_name,last_name=last_name,email=email,username=username, profile_img=profile_pic)
    user.set_password(password)
    user.save()
    login_auth(request,user)
    return HttpResponseRedirect(reverse('Khal_Ture:index'))
  else:
    return HttpResponseRedirect(reverse('Khal_Ture:signup'))
    
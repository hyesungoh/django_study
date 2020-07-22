from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from .forms import PostForm, SigninForm

from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.http import HttpResponse

# Create your views here.
def main(request):
    posts = Post.objects.all()
    signin_form = SigninForm()
    return render(request, 'appname/main.html', {'posts': posts, 'signin_form': signin_form})

def create(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form = form.save(commit=False)
            form.save()
            return redirect('main')
    else:
        form = PostForm()
        return render(request, 'appname/create.html', {'form': form})

def read(request):
    return redirect('main')

def update(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form = form.save(commit=False)
            form.save()
            return redirect('main')
    else:
        form = PostForm(instance=post)
        return render(request, 'appname/create.html', {'form': form})

def delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('main')

def signin(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username = username, password = password)

        if user is not None:
            login(request, user)
            return redirect('main')
        else:
            return HttpResponse("로그인 실패. 다시 시도해보세요 ㅋ")

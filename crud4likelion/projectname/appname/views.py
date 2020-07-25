from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, CustomUser
from .forms import PostForm, SigninForm, UserForm, CommentForm

# from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.http import HttpResponse

# Create your views here.
def main(request):
    posts = Post.objects.all()
    signin_form = SigninForm()
    comment_form = CommentForm()
    return render(request, 'appname/main.html', {'posts': posts, 'signin_form': signin_form,
    'comment_form': comment_form})

def create(request):
    if not request.user.is_active:
        return HttpResponse("You can write a post with SIGNIN")

    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form = form.save(commit=False)
            form.writer = request.user
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

def comment(request, post_id):
    if not request.user.is_active:
        return HttpResponse("You can write a post with SIGNIN")

    post = get_object_or_404(Post, id=post_id)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.c_writer = request.user
            comment.post_id = post
            comment.text = form.cleaned_data['text']
            comment.save()
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

def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            new_user = CustomUser.objects.create_user(username=form.cleaned_data['username'],
            email=form.cleaned_data['email'],
            password=form.cleaned_data['password'],
            nickname=form.cleaned_data['nickname'],
            phone_number=form.cleaned_data['phone_number'])
            login(request, new_user)
            return redirect('main')
    else:
        form = UserForm()
        return render(request, 'appname/signup.html', {'form': form})

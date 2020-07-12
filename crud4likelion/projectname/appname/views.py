from django.shortcuts import render, redirect
from .models import Post
from .forms import CreateForm

# Create your views here.
def main(request):
    posts = Post.objects.all()
    return render(request, 'appname/main.html', {'posts': posts})

def create(request):
    if request.method == "POST":
        form = CreateForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.save()
            return redirect('main')
    else:
        form = CreateForm()
        return render(request, 'appname/create.html', {'form': form})

def read(request):
    return redirect('main')

def update(request):
    return redirect('main')

def delete(request):
    return redirect('main')

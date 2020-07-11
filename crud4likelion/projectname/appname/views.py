from django.shortcuts import render, redirect

# Create your views here.
def main(request):
    return render(request, 'appname/main.html')

def create(request):
    return render(request, 'appname/create.html')

def read(request):
    return redirect('main')

def update(request):
    return redirect('main')

def delete(request):
    return redirect('main')

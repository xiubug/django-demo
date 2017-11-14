from django.shortcuts import render


def index(request):
    return render(request, 'blog2/index.html')

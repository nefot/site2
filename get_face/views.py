from django.shortcuts import render

# Create your views here.
def geting(request):

    return render(request, 'blog/header.html')

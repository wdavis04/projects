from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    #return HttpResponse('HELLO FROM POSTS')

    return render(request, 'posts/layout.html')
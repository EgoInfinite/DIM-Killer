from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'username': 'EgoInfinite',
        'password': 'Password'
    }    
]

def goto_landing(request):
    context = {
        'posts': posts    
    }
    return render(request, 'test_template.html', context)

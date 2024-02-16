from django.shortcuts import render

# Create your views here.

posts = [
    {
        'author': 'Billy',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'data_posted': 'August 27,2023'
    },
    {
        'author': 'John',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'data_posted': 'December 27,2023'
    }
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})

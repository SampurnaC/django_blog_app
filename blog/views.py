from django.shortcuts import render
# Create your views here.

posts = [
    {
        'author': 'Sam',
        'title': 'Title 1',
        'content': 'First post content',
        'date_posted': 'August 10, 2022'
    },
    {
        'author': 'Sam1',
        'title': 'Title 2',
        'content': 'First post content 1',
        'date_posted': 'August 10, 2022'
    }
]
def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)
    # return HttpResponse('<h1>Blog Home</h1>')

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})


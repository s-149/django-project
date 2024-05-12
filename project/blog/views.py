from django.shortcuts import render

from .models import Post


def index(request):
    posts = Post.objects.all()
    print(posts)
    context = {
        'title': 'Blog',
        'heading': 'Blog',
        'subheading': 'jurnal kelas terbuka',
        'Post': posts,
    }
    return render(request, 'blog/index.html', context)

# def news(request):
#     context = {
#         "title" : "News",
#         "description" : "News django",
#     }
#     return render(request, 'blog/index.html', context)

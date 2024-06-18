from django.shortcuts import render
from .models import Blog

# Create your views here.
def blog(request):
    context = {
        'posts': Blog.objects.all().order_by('-created_at')
    }
    return render(request, 'blog/blog.html', context)

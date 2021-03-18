from django.shortcuts import render,get_object_or_404
from .models import Blog

# Create your views here.

def index(request):
    var_1 = Blog.objects.all()
    return render(request, 'blog/index.html', {'var_1':var_1})


def detail(request, blog_id):
    detail_home = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/post.html', {'detail_home': detail_home})




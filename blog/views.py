from django.shortcuts import render
from .models import Post # dot means current dir
from django.utils import timezone
from django.shortcuts import render, get_object_or_404

# Create your views here.
# takes request then return with the render function that will show template
# posts is QuerySet's name here
# {} parameter: in this rendered document, variable posts indicates QuerySet posts
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})


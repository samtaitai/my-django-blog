from django.shortcuts import render

# Create your views here.
# takes request then return with the render function that will show template
def post_list(request):
    return render(request, 'blog/post_list.html', {})

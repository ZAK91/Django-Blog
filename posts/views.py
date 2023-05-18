from django.shortcuts import render

# Create your views here.

def post_list(request):
    data = post.objects.all()
    return render(request,'posts/posts.html'{})
from django.shortcuts import render
from .models import Post
from .forms import PostForm
# Create your views here.

def post_list(request):
    data = Post.objects.all()
    return render(request,'posts/posts.html',{'posts':data})

def post_detail(request,post_id):
    data = Post.objects.get(id=post_id)
    return render(request,'posts/detail.html',{'post':data})


def new_post(request):
    form = PostForm()
    return render(request,'posts/new.html',{'form':form})
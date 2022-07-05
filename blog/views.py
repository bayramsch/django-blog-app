from xml.etree.ElementTree import Comment
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect

from .models import BlogPost, Like, ViewPost
from .forms import BlogPostForm, CommentForm
from pprint import pprint
from django.contrib.auth.decorators import login_required
from django.contrib import messages 

def postList(request):
    # posts = BlogPost.objects.all()
    posts = BlogPost.objects.filter(status="p")
    
    context = {
        'posts':posts
    }

    return render(request,'blog/postList.html', context)



@login_required()
def postCreate(request):
    form = BlogPostForm()
    if request.method == "POST":
        form = BlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            messages.success(request,"Post created succesfully!")
            return redirect('blog:postlist')
    
    context = {
        "form":form
    }
    
    return render(request,"blog/postCreate.html", context)


def postDetail(request, slug):
    # pprint(request)
    form = CommentForm()
    detailobj = get_object_or_404(BlogPost, slug=slug)
    if request.user.is_authenticated:
        ViewPost.objects.get_or_create(user=request.user, post=detailobj)
    
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.post = detailobj
            comment.save()
            return redirect('blog:postdetail', slug=slug)
            # return redirect(request.path)
    context = {
        'detailobj':detailobj,
        'form':form
    }
    
    return render(request, 'blog/postDetail.html', context)

@login_required()
def postUpdate(request, slug):
    updateobj = get_object_or_404(BlogPost, slug=slug)
    form = BlogPostForm(request.POST or None, request.FILES or None, instance=updateobj)
    if request.user.id != updateobj.author.id:
        messages.warning(request,"You are not a writer of this post!")
        return redirect('blog:postlist')
    
    if form.is_valid():
        form.save()
        return redirect('blog:postlist')
    
    context = {
        "updateobj":updateobj,
        "form":form
    }     
    
    return render(request,'blog/postUpdate.html', context)

@login_required()
def postDelete(request, slug):
    deleteobj = get_object_or_404(BlogPost, slug=slug)
    if request.user.id != deleteobj.author.id:
        return HttpResponse("You are not authorized!!")
    if request.method == "POST":
        deleteobj.delete()
        messages.success(request,"Post deleted succesfully!")
        return redirect("blog:postlist")
    context = {
        "deleteobj":deleteobj
    }
    
    return render(request, 'blog/postDelete.html', context)


@login_required()
def like(request, slug):
    if request.method == "POST":
        obj = get_object_or_404(BlogPost, slug=slug)
        like_st = Like.objects.filter(user=request.user, post=obj)
        if like_st.exists():
            like_st[0].delete()
        else:
            Like.objects.create(user=request.user, post=obj)
        
    return redirect('blog:postdetail', slug=slug )
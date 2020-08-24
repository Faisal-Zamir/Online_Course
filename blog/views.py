from django.shortcuts import render, redirect, HttpResponseRedirect
from .forms import PostForm, CommentForm
from .models import Post, Comment


def BlogHome(request):
    posts = Post.objects.all().order_by('-id')
    context  = {'posts':posts}
    return render(request, 'blog/blog_home.html',context)

def rafpage(request):
    return render(request, 'blog/rafpage.html')

def BlogForm(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            user_post = form.save(commit=False)
            user_post.author = request.user
            user_post.save()
            return redirect('blog-home')
    else:
        form = PostForm()
    context = {'form':form}
    return render(request, 'blog/post_form.html',context)

def PostDetails(request,id):
    post = Post.objects.get(id=id)
    comments = post.comments.all().order_by("-created_on")
    # Comment posted
    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            
            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            # Save the comment to the database
            new_comment.save()
            comment_form = CommentForm()

    else:
        comment_form = CommentForm()

    context ={"post": post,"comments": comments,
         
            "comment_form": comment_form}
    
    return render(request, 'blog/post_details.html',context)
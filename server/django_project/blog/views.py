from django.shortcuts import render,get_object_or_404, redirect
from .models import Post
from .forms import PostForm
from django.utils import timezone

def posts(request):
    posts = Post.objects.filter(published_at__isnull=False).order_by('-published_at')
    return render(request, 'blog/posts.html', {'posts': posts})

def post_detail(request, id):
	post = get_object_or_404(Post, id=id)
	return render(request, 'blog/post_detail.html',{'post':post})

def post_create(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_at = timezone.now()
            post.save()
            return redirect('post_detail', id=post.id)
    else:
        form = PostForm()
    return render(request, 'blog/post_create.html', {'form': form})
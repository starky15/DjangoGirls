from django.shortcuts import render ,get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Post
from .forms import PostForm
from django.utils import timezone

@login_required(login_url='login')
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts':posts})
def post_my(request):
    user = User.objects.get(username=request.user)
    posts = Post.objects.all().filter(author=user).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

# Create your views here.
def post_detail(request, pk):
    post = get_object_or_404(Post,pk=pk)
    return render(request, 'blog/post_detail.html', {'post':post})

def post_delete(request, pk):
    post = get_object_or_404(Post,pk=pk)
    post.delete()
    return redirect('post_list')
@login_required(login_url='login')
def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail' ,pk=post.pk)


    else:
        form = PostForm()
        return render(request, 'blog/post_edit.html',{'form':form})

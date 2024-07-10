from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post, Form
from .forms import PostForm, SaveForm

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})

def create_form(request):
    context = {}
    context['form'] = SaveForm()
    return render(request, "blog/show_form.html", context)

def form_list(request):
    posts = Form.objects.all()
    return render(request, 'blog/form_list.html', {'forms': posts})

def form_detail(request, pk):
    form = get_object_or_404(Form, pk=pk)
    return render(request, 'blog/form_detail.html', {'form': form})

def form_edit(request, pk):
    post = get_object_or_404(Form, pk=pk)
    if request.method == "POST":
        form = SaveForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('form_detail', pk=post.pk)
    else:
        form = SaveForm(instance=post)
    return render(request, 'blog/form_edit.html', {'form': form})
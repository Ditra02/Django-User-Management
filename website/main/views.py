from django.shortcuts import render, HttpResponse, redirect
from .forms import RegisterForm, PostForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required, permission_required
from .models import Post


@login_required(login_url="/login")
def home(request):
    posts = Post.objects.all()
    
    if request.method == "POST":
        post_id = request.POST.get("post-id")
        post = Post.objects.filter(id=post_id).first()
        
        if post and post.author == request.user:
            post.delete()
    
    context = {'posts' : posts}
    
    return render(request=request, template_name='main/home.html', context=context)


@login_required(login_url="/login")
@permission_required("add_post", login_url='/login', raise_exception=True)
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        
        if form.is_valid():
            # prevent the post saved in the database
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect("/home")
    else:
        form = PostForm()
        
    return render(request=request, template_name='main/create_post.html', context={'form':form})


def sign_up(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        
        if form.is_valid():
            user = form.save()
            login(request=request, user=user)
            return redirect('/home')

    else:
        form = RegisterForm()

    return render(request=request, template_name='registration/sign_up.html', context={'form': form})

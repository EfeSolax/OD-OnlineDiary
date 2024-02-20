from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import BlogModel, CommentModel
from .forms import BlogForm
from django.contrib import messages

# Create your views here.

def index(request):
    return render(request, "index.html")

def about(request):
    return render(request, "about.html")

@login_required(login_url="/user/login/")
def control_panel(request):
    all_blogs = BlogModel.objects.filter(author = request.user)

    comments = list()

    for blog in all_blogs:
        
        for comment in blog.comments.all():
            comments.append(comment)

    context = {
        "blogs": all_blogs,
        "comments": comments
    }

    return render(request, "control_panel.html", context)

def add_blog(request):
    form = BlogForm(request.POST or None)

    if form.is_valid():
        blog = form.save(commit=False)
        blog.author = request.user
        blog.save()
        messages.success(request, "Günlüğünüz başarıyla eklendi.")
        return redirect("control_panel")

    
    return render(request, "add_blog.html", {"form": form})

@login_required(login_url="/user/login/")
def delete_blog(request, id):   
    blog = get_object_or_404(BlogModel ,id = id)

    if request.user.username == blog.author.username:
        blog.delete()
        messages.success(request, "Günlüğünüz başarıyla silindi")
    else:
        messages.info(request, "Günlük size ait olmadığı için silinemedi")

    return redirect("control_panel")

@login_required(login_url="/user/login/")
def update_blog(request, id):
    article = get_object_or_404(BlogModel, id = id)
    
    form = BlogForm(request.POST or None, instance=article)

    if form.is_valid():
        blog = form.save(commit=False)
        blog.author = request.user
        blog.save()
        messages.success(request, 'Günlük  güncellendi')
        return redirect('control_panel') 

    return render(request, 'update.html', {"form": form})

def diaries(request):
    all_diaries = BlogModel.objects.all()

    keyword = request.GET.get('keyword')

    if keyword:
        all_diaries = BlogModel.objects.filter(title__contains=keyword)

        return render(request, 'diaries.html', {"blogs": all_diaries})

    return render(request, "diaries.html", {"blogs": all_diaries})

def detail(request, id):
    blog = get_object_or_404(BlogModel, id=id)

    comments = blog.comments.all()

    return render(request, "detail.html", {"blog": blog, "comments": comments})

@login_required(login_url="/user/login/")
def add_comment(request, id):
    blog = get_object_or_404(BlogModel, id=id)

    if request.method == 'POST':
        comment_content = request.POST.get('comment_content')

        if len(comment_content) > 250:
            messages.info(request, "Yorum 250 karakterden büyük olamaz")
            return redirect('/blogs/detail/' + str(id))

        newComment = CommentModel(comment_author=request.user, comment_content=comment_content)
        newComment.article = blog
        newComment.save()

        messages.success(request,"Yorum Eklendi")
        
    return redirect('/blogs/detail/' + str(id)) 

@login_required(login_url = "7user/login/")
def delete_comment(request,id, id2):
    blog = get_object_or_404(BlogModel, id = id)
    comments = blog.comments.all()

    for comment in comments:        
        if comment.id == id2:
            comment.delete()
            messages.success(request, "Yorum silindi")

    return redirect("/blogs/detail/" + str(id))

def surf(request):
    all_blogs = BlogModel.objects.all()

    keyword = request.GET.get('keyword')

    if keyword:
        all_blogs = BlogModel.objects.filter(title__contains=keyword)
        return render(request, 'surf.html', {'blogs': all_blogs})


    return render(request, "surf.html", {"blogs": all_blogs})

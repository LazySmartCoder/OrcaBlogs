from django.shortcuts import render, HttpResponse, redirect
from .models import *
from datetime import datetime
def index(request):
    bvar = BlogPost.objects.all()
    param = {
        "blogs" : bvar, "single" : bvar.last()
        }
    return render(request, "index.html", param)

def ErrorOccured(request):
    return render(request, "error.html")

def ErrorPage(request, exception):
    return render(request, "error.html")

def Blogs(request):
    bvar = BlogPost.objects.all()
    param = {"blogs" : bvar}
    return render(request, "blogs.html", param)

def ReadBlogs(request, bslug):
    bvar = BlogPost.objects.all()
    blogs = BlogPost.objects.get(BlogSlug = bslug)
    com = PostComment.objects.filter(PostID = blogs.BlogID)
    blogs.Views = int(blogs.Views) + 1
    blogs.save()
    return render(request, "reader.html", {
        "name" : blogs.BlogName, "date" : blogs.BlogDateAdded,
        "desc" : blogs.BlogDescription,
        "image" : blogs.BlogImage,
        "cat" : blogs.BlogCategory,
        "post" : blogs.BlogPost,
        "author" : blogs.BlogAuthor,
        "views" : blogs.Views,
        "likes" : blogs.Likes.count, 
        "blogid" : blogs.id,
        "views" : blogs.Views,
        "keywords" : blogs.BlogKeywords,
        "slug" : blogs.BlogSlug,
        "comments" : com,
        "countcomm" : com.count(),
        "blogs" : bvar,
    })

def Comment(request, comsl):
    bvar = BlogPost.objects.get(BlogSlug = comsl)
    name = request.POST["name"]
    email = request.POST["email"]
    message = request.POST["message"]
    createComment = PostComment(PostID = bvar.BlogID, Name = name, Email = email, Message = message, Date = datetime.now())
    createComment.save()
    return redirect(f"/{comsl}#comm")

def Category(request, catl):
    bvar = BlogPost.objects.filter(BlogCategory = catl)
    return render(request, "cat.html", {"cat" : bvar, "catname" : catl.replace("-", " "), "blogs" : BlogPost.objects.all()})


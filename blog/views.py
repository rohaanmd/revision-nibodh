from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import blog
def home(request):
    List = blog.objects.all()

    params = {
        "data" : List
    }
    return render(request,"blog/index.html",params)

def createView(request):
    return render(request,"blog/create.html")

def editView(request,id):

    Blog = blog.objects.get(id=id)
    print(Blog)
    return render(request,"blog/edit.html",{"blog":Blog})


def createBlog(request):
    name = request.POST.get("title")
    body = request.POST.get("body") 
    myfile = request.FILES['image']
    NewBlog = blog(title=name , body=body , image=myfile)
    NewBlog.save()
    return redirect("/blog/")
    
def editBlog(request,id):
    
    UpdatingBlog = blog.objects.get(id=id)

    UpdatingBlog.title = request.POST.get("title")
    UpdatingBlog.body = request.POST.get("body") 
    print(request.FILES)
    if request.FILES:
        UpdatingBlog.image = request.FILES['image']

    UpdatingBlog.save()
    return redirect("/blog/")

def deleteBlog(request,id):
    Blog = blog.objects.get(id=id)
    Blog.delete()
    return redirect("/blog/")



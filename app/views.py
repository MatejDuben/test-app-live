from django.shortcuts import redirect, render

from django.http import HttpResponse

from .models import Post
from .form import AddPostForm

# Create your views here.



def main(request):

    posts = Post.objects.all()
    form = AddPostForm(request.POST or None)

    
    if request.method == "POST":
        if form.is_valid():
            form.save()

            return redirect('home_page')
            

    context = {
        "form": form,
        "posts": posts
    }
    return render(request,'home.html', context)
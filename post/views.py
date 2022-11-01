from django.shortcuts import render
from .models import Post
from django.views.generic import ListView , DetailView , CreateView , DeleteView , UpdateView

# Create your views here.

class Post_List(ListView):
    model = Post

class Post_Detail(DetailView):
    model = Post

class Post_Create():
    pass

class Post_Delete():
    pass

class Post_Update():
    pass
'''
def post_list(request):
    
    post_list = Post.objects.all()
    context = {'list':post_list}
    return render (request , 'post/list.html' , context)


def post_detail(request):
    pass
'''
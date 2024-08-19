from django.forms import BaseModelForm
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.db.models import Q
from .models import Post
from .forms import PostForm
from django.views.generic import DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
# Create your views here.

def index(request):
    context = {}
    if len(request.GET) != 0:
        query = request.GET.get('q')
        posts = Post.objects.filter(
            Q(title__icontains = query) |
            Q(desc__icontains = query)
        )
        context['posts'] = posts
        return render(request,"Blogapp/index.html",context)
    context['posts'] = Post.objects.all()
    return render(request,"Blogapp/index.html",context)
    

class PostView(DetailView):
    model = Post
    template_name = "Blogapp/post.html"
    context_object_name = "post"
    
class CreatePost(CreateView):
    form_class = PostForm
    template_name = "Blogapp/createPost.html"
    success_url = reverse_lazy('index')
    
class UpdatePost(UpdateView):
    model = Post
    template_name = "Blogapp/createPost.html"
    fields = "__all__"
    success_url = reverse_lazy('index')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["view_name"] = "update"
        return super().get_context_data(**kwargs)
    
class DeletePost(DeleteView):
    model = Post
    template_name = "Blogapp/deletePost.html"
    success_url = reverse_lazy('index')
    
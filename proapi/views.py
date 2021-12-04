from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView
from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Post
from .serializer import PostSerializer
from django.urls import reverse_lazy

# Create your views here.
class ApiPageView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostList(ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostDetail(RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class IndexPageView(TemplateView):
    template_name = 'index.html'

class HomePageView(ListView):
    model = Post
    template_name = 'home.html'

class CreatePageView(CreateView):
    model = Post
    template_name = 'create.html'
    fields = ['name', 'email', 'password']

class EditPageView(UpdateView):
    model = Post
    template_name = 'edit.html'
    fields = ['name','email','password']

class DeletePageView(DeleteView):
    model = Post
    template_name = 'delete.html'
    success_url = reverse_lazy('home')
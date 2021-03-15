from django.views.generic import ListView
from .models import Post

class HomePageView(ListView):
    """docstring for HomePageView"""
    model = Post
    template_name = 'home.html'
    context_object_name = 'all_posts_list'

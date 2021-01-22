from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post, Category


class BlogView(ListView):
    model = Post
    template_name = 'blog/blog.html'
    ordering = ['-id']

    # list of categories for blog home page "blog categories" list
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories_list'] = Category.objects.all().order_by('name')
        return context

class BlogContentView(DetailView):
    model = Post
    template_name = 'blog/blog_content.html'

def CategoryView(request, cats):
    category_posts = Post.objects.filter(slug=cats)
    context = {'cats':cats, 'category_posts':category_posts}  
    return render(request, 'blog/categories.html', context)



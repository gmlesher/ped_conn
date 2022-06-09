from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import BlogIndexPage, BlogPage


class BlogView(ListView):
    model = BlogIndexPage
    template_name = 'blog/blog_index_page.html'
    ordering = ['-id']

    # list of categories for blog home page "blog categories" list
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories_list'] = BlogPage.objects.all().order_by('name')
        return context


class BlogContentView(DetailView):
    model = BlogPage
    template_name = 'blog/blog_page.html'


def CategoryView(request, cats):
    category_posts = BlogIndexPage.objects.filter(slug=cats)
    context = {'cats': cats, 'category_posts': category_posts}
    return render(request, 'blog/categories.html', context)

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Article, Category, Tag

# Create your views here.
def index(request):
    article_list = Article.objects.all().order_by('-created_time')
    category_list = Category.objects.all()

    return render(request, 'longfellow/index.html', context={'article_list': article_list,
        'category_list': category_list})

def category(request, pk):
    category_list = get_object_or_404(Category, pk=pk)
    
    return render(request, 'longfellow/category.html', context={'category_list': category_list})

def about(request):
    return render(request, 'longfellow/about.html')

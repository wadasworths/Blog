from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Article, Category, Tag
import markdown

# Create your views here.
def index(request):
    article_list = Article.objects.all().order_by('-created_time')
    category_list = Category.objects.all()

    return render(request, 'longfellow/index.html', context={'article_list': article_list,
        'category_list': category_list})

def category(request):
    category_list = Category.objects.all()
    
    return render(request, 'longfellow/category.html', context={'category_list': category_list})

def about(request):
   category_list = Category.objects.all()
   return render(request, 'longfellow/about.html', context={'category_list': category_list})

def detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    article.content = markdown.markdown(article.content,
                                        extensions=[
                                            'markdown.extensions.extra',
                                            'markdown.extensions.codehilite',
                                            'markdown.extensions.toc',
                                        ])
    category_list = Category.objects.all()

    return render(request, 'longfellow/detail.html', context={'article': article,
        'category_list': category_list})

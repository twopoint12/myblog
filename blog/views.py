import markdown
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from .models import Article, Category


# Create your views here.
def index(request):
    article_list = Article.objects.all().order_by('-created_time')
    return render(request, 'blog/index.html', context={
        'article_list': article_list
    })


def detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    article.body = markdown.markdown(article.body, extensions=[
        'markdown.extensions.extra',
        'markdown.extensions.codehilite'
    ])
    return render(request, 'blog/detail.html', context={
        'article': article
    })


def archives(request, year, month):
    article_list = Article.objects.filter(created_time__year=year,
                                          created_time__month=month
                                          ).order_by('-created_time')
    return render(request, 'blog/index.html', context={
        'article_list': article_list
    })


def category(request, pk):
    cate = get_object_or_404(Category, pk=pk)
    article_list = Article.objects.filter(category=cate).order_by('-created_time')
    return render(request, 'blog/index.html', context={'article_list': article_list})


def update_likes(request):
    if request.method == 'POST':
        article_id = request.POST['articleId']
        likes = request.POST['likes']
        likes = int(likes) + 1
        Article.objects.filter(id=article_id).update(likes=likes)
        return JsonResponse({"status": "Complete", "likes": likes}, safe=False)


def about_site(request):
    return render(request, 'blog/about_site.html')


def about_me(request):
    return render(request, 'blog/about_me.html')
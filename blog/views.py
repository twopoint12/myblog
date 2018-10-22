import markdown
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from .models import Article, Category, Like


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
        article = Article.objects.get(id=article_id)
        ip = get_ip(request)
        insert_success = Like.objects.get_or_create(ip=ip, article=article)[1]
        if insert_success:
            json_response = JsonResponse({"status": "insert success"}, safe=False)
        else:
            json_response = JsonResponse({"status": "insert fail"}, safe=False)
        return json_response


def get_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]  # 所以这里是真实的ip
    else:
        ip = request.META.get('REMOTE_ADDR')  # 这里获得代理ip
    return ip


def my_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]  # 所以这里是真实的ip
    else:
        ip = request.META.get('REMOTE_ADDR')  # 这里获得代理ip
    return HttpResponse("<h1>Your ip is: %s</h1>" % ip)


def about_site(request):
    return render(request, 'blog/about_site.html')


def about_me(request):
    return render(request, 'blog/about_me.html')

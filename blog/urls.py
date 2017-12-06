from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^article/(\d+)/$', views.detail, name='detail'),
    url(r'^archives/(\d{4})/(\d{1,2})/$', views.archives, name='archives'),
    url(r'^category/(\d+)/$', views.category, name='category'),
    url(r'^update_likes/$', views.update_likes, name='update_likes'),
    url(r'^about_site/$', views.about_site, name='about_site'),
    url(r'^about_me/$', views.about_me, name='about_me')
]
from django.conf.urls import url
from . import views

app_name = 'longfellow'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.detail, name='detail'),
    url(r'^about.html$', views.about, name='about'),
    url(r'^category.html$', views.category, name='category')
]

from django.conf.urls import url

from zapp import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^users/$', views.users, name='users'),
    url(r'^transfer/$', views.transfer, name='transfer'),
    url(r'^zoobar.js$', views.zoobarjs, name='zoobarjs'),
]

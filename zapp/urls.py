from django.conf.urls import url

from zapp import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^user/(?P<user_id>[0-9]+)/$', views.user, name='user'),
    url(r'^users/$', views.users, name='users'),
    url(r'^transfer/$', views.transfer, name='transfer'),
]

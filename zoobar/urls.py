from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^/?', include('zapp.urls')),
    url(r'^accounts/', include('zlogio.urls')),
)

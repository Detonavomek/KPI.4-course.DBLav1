from django.conf.urls import patterns, include, url

from main import views as main_views

urlpatterns = patterns(
    '',
    url(r'^$', main_views.home, name='home'),
    url(r'^add/$', main_views.add, name='add'),
)

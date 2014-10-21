from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'Laba1.views.index', name='index'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^account/', include('Laba1.urls')),
    url(r'^admin/', include(admin.site.urls)),
)

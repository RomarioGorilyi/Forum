from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'FirApp.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^basicview/', include('article.urls')),  #не нужно
    url(r'^auth/', include('loginsys.urls')),
    url(r'^', include('article.urls')),			#порядок имеет значение
)

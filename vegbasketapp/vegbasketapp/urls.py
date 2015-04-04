from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings


urlpatterns = patterns('',
    url(r'^$', 'vegbasketapp.home.views.index', name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^e404$', 'vegbasketapp.home.views.handler404'),
    url(r'^e500$', 'vegbasketapp.home.views.handler500'),
    url(r'^transformer/entry/(?P<region_id>.*)$', 'vegbasketapp.transformer.views.region', name='region'),
    url(r'^transformer/entry/(?P<entry_id>.*)$', 'vegbasketapp.transformer.views.entry', name='entry'),
    url(r'^transformer/entry/(?P<entry_id>.*)/map$', 'vegbasketapp.transformer.views.entry_map', name='map'),


)

urlpatterns += patterns('',
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    )

# handler404 = 'vegbasketapp.home.views.handler404'
# handler500 = 'vegbasketapp.home.views.handler500'


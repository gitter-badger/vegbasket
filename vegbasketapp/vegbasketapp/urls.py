from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views


urlpatterns = patterns('',
    url(r'^$', 'vegbasketapp.home.views.index', name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^e404$', 'vegbasketapp.home.views.handler404'),
    url(r'^e500$', 'vegbasketapp.home.views.handler500'),
    url(r'^transformer/entry/(?P<entry_id>\d*)/reviews$', 'vegbasketapp.transformer.views.entry_reviews', name='reviews'),
    url(r'^transformer/entry/(?P<entry_id>\d*)/map$', 'vegbasketapp.transformer.views.entry_map', name='map'),
    url(r'^transformer/entry/(?P<entry_id>.*)$', 'vegbasketapp.transformer.views.entry', name='entry'),
    url(r'^transformer/region/(?P<region_id>.*)$', 'vegbasketapp.transformer.views.region', name='region'),
    url(r'^transformer/region$', 'vegbasketapp.transformer.views.region_root', name='region_root'),
    url('', include('social.apps.django_app.urls', namespace='social')),    
    url(r'^accounts/setup/$', 'vegbasketapp.personal.views.accounts_setup', name='accounts_setup'),
    url(r'^p/$', 'vegbasketapp.personal.views.personal', name='personal'),
    url('^logout/', auth_views.logout_then_login, {'login_url':"/login/"}),
    url('^', include('django.contrib.auth.urls'))
)

urlpatterns += patterns('',
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    )

# handler404 = 'vegbasketapp.home.views.handler404'
# handler500 = 'vegbasketapp.home.views.handler500'


from django.conf.urls import include, url
from django.contrib import admin
from api import views as api_views
from account import views as account_views

urlpatterns = [
    # Examples:
    # url(r'^$', 'swaggerTest.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/$', api_views.index),
    url(r'^api/docs/$', api_views.docs),
    url(r'^api/docs/(?P<json>\w+)/$', api_views.module),

    url(r'^api/account/login$', account_views.api_account_login),

]

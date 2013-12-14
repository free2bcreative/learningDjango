from django.conf.urls import patterns, include, url
from mysite.views import another_page, hello, my_homepage_view, current_datetime, hours_ahead, logged_in

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', my_homepage_view),
    url(r'^another/page/$', another_page),
    url(r'^time/$', current_datetime),
    url(r'^time/plus/(\d{1,2})/$', hours_ahead),
    url(r'^login/$', logged_in),

    url(r'^admin/', include(admin.site.urls)),
    
    # 'r' makes the string a "raw string" - you don't have to worry about escaping the backslashes
    # '^' says that it must start with 'hello/'
    # '$' says that it must end with 'hello/'
    #	The use of both ^ and $ makes it so Django matches that url letter for letter
    url(r'^hello/$', hello),
)

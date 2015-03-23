from django.conf.urls import patterns, url
from MyStreet import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^about/$', views.about, name='about'),
     url(r'^search/$', views.search, name='search'),
    url(r'^add_street/$', views.add_street, name='add_street'),
    url(r'^street/(?P<street_name_slug>[\w\-]+)/$', views.street, name='street'),
    url(r'^street/(?P<street_name_slug>[\w\-]+)/add_comment/$', views.add_comment, name='add_comment'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^safetylist/$', views.safetylist, name='safetylist'),
    url(r'^businesslist/$', views.businesslist, name='businesslist'),
    url(r'^infrastructurelist/$', views.infrastructurelist, name='infrastructurelist'),
    url(r'^alllist/$', views.alllist, name='alllist'),

)



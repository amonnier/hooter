from django.conf.urls import patterns, include, url

from hooter_app import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	url(r'^(?P<pseudo>\w+)/$',views.profile_view, name='profile_view'),

)

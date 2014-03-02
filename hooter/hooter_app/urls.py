from django.conf.urls import patterns, include, url

from hooter_app import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	url(r'^connexion$',views.connexion,name='connexion'),
	url(r'^deconnexion$',views.deconnexion,name='deconnexion'),
	url(r'^enregistrement$',views.enregistrement,name='enregistrement'),
	url(r'^(?P<pseudo>\w+)/$',views.profile_view, name='profile_view'),
	url(r'^(?P<pseudo>\w+)/settings',views.modif_profil,name='modif_profil'),

)

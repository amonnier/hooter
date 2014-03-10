from django.conf.urls import patterns, include, url

from hooter_app import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	url(r'^connexion$',views.connexion,name='connexion'),
	url(r'^recuperation_mot_de_passe$',views.recup_pass,name='recuperation_mot_de_passe'),
	url(r'^deconnexion$',views.deconnexion,name='deconnexion'),
	url(r'^recherche$',views.rechercher,name='recherche'),
	url(r'^enregistrement$',views.enregistrement,name='enregistrement'),
	url(r'^#(?P<hashtag>\w+)$',views.afficher_hashtag, name='afficher_hashtag'),
	url(r'^hashtag/(?P<hashtag>\w+)$',views.afficher_hashtag, name='afficher_hashtag_full'),
	url(r'^(?P<pseudo>\w+)/$',views.profile_view, name='profile_view'),
	url(r'^(?P<pseudo>\w+)/settings',views.modif_profil,name='modif_profil'),
	url(r'^enregistrer_profil$',views.enregistrer_profil,name='enregistrer_profil'),
	url(r'^suivre(?P<pseudo>\w+)$',views.suivre,name='suivre'),
	url(r'^envoyer_message$',views.envoyer_message,name='envoyer_message'),	
	url(r'^sedesabonner(?P<pseudo>\w+)$',views.sedesabonner,name='sedesabonner'),
	url(r'^(?P<pseudo>\w+)/password$',views.modif_password,name='modif_password'),
	url(r'^(?P<pseudo>\w+)/abonnes',views.liste_abonnes,name='liste_abonnes'),
	url(r'^(?P<pseudo>\w+)/abonnements',views.liste_abonnements,name='liste_abonnements'),
	url(r'^supprimer(?P<id_message>\w+)$',views.supprimer,name='supprimer'),
		
)

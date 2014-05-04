# -*-coding:utf-8 -*
from django.db import models
from django.utils.safestring import SafeUnicode


#representation d'un utilisateur en base
class Utilisateur(models.Model):
	pseudo=models.CharField(max_length=20,unique=True)#son pseudo, unique, cle primaire
	nom=models.CharField(max_length=20)
	mot_passe=models.CharField(max_length=50)
	email=models.CharField(max_length=50,unique=True)
	pays=models.CharField(max_length=50)
	ville=models.CharField(max_length=50)
	date_naiss=models.DateField()
	photo=photo = models.ImageField(upload_to="photos/",blank=True, null=True,default="photos/default.jpeg")
	#lien many-to-many vers utilisateurs pour les abonnements
	abonnements=models.ManyToManyField("Utilisateur",blank=True,related_name="abonnements+")
	#lien many-to-many vers utilisateurs pour les abonnes
	abonnes=models.ManyToManyField("Utilisateur",blank=True,related_name="abonnes+")

	def __unicode__(self):
	        return self.pseudo

#representation d'un tweet
class Message(models.Model):
	contenu=models.CharField(max_length=140)
	date=models.DateTimeField()
	utilisateur=models.ForeignKey(Utilisateur)#l'utilisateur actuel du message
	utilisateur_createur=models.ForeignKey(Utilisateur,related_name="utilisateur_createur+", null=True)#l'utilisateur qui a créé le message en premier
	hashtags=models.ManyToManyField("Hashtag", blank=True)

	def __unicode__(self):
	        return SafeUnicode(self.contenu)[0:15]

#representation d'un hashtag
class Hashtag(models.Model):
	nom=models.CharField(max_length=20)
	messages=models.ManyToManyField(Message, blank=True)

	def __unicode__(self):
	        return self.nom




	

	


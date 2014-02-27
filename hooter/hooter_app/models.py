from django.db import models
from django.utils.safestring import SafeUnicode

# Create your models here.

class Utilisateur(models.Model):
	pseudo=models.CharField(max_length=20)
	mot_passe=models.CharField(max_length=50)
	email=models.CharField(max_length=50)
	pays=models.CharField(max_length=50)
	ville=models.CharField(max_length=50)
	date_naiss=models.DateField()
	photo=models.CharField(max_length=100,blank=True)
	abonnements=models.ManyToManyField("self",blank=True)

	def __unicode__(self):
	        return self.pseudo

class Message(models.Model):
	contenu=models.CharField(max_length=140)
	date=models.DateField()
	utilisateur=models.ForeignKey(Utilisateur)
	hashtags=models.ManyToManyField("Hashtag", blank=True)

	def __unicode__(self):
	        return SafeUnicode(self.contenu)[0:15]

class Hashtag(models.Model):
	nom=models.CharField(max_length=20)
	messages=models.ManyToManyField(Message, blank=True)

	def __unicode__(self):
	        return self.nom




	

	


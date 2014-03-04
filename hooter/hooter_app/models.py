from django.db import models
from django.utils.safestring import SafeUnicode

# Create your models here.

class Utilisateur(models.Model):
	pseudo=models.CharField(max_length=20,unique=True)
	nom=models.CharField(max_length=20)
	mot_passe=models.CharField(max_length=50)
	email=models.CharField(max_length=50,unique=True)
	pays=models.CharField(max_length=50)
	ville=models.CharField(max_length=50)
	date_naiss=models.DateField()
	photo=photo = models.ImageField(upload_to="photos/",blank=True, null=True,default="photos/default.jpeg")
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




	

	


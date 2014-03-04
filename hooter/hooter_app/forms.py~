# coding = utf-8

from django import forms
from hooter_app.models import Utilisateur
from django.forms.extras.widgets import SelectDateWidget

class ConnexionForm(forms.ModelForm):
	
	email = forms.EmailField(required=True,widget=forms.EmailInput(attrs={'placeholder': 'Email','class' : 'form-control'}),label='')
	mot_passe = forms.CharField(required=True,widget=forms.PasswordInput(attrs={'placeholder': 'Mot de passe','class' : 'form-control'}),label='')
	class Meta:
		model = Utilisateur
		fields = ['email','mot_passe']
	def validate_unique(self):
		pass
		
class RecupPassForm(forms.ModelForm):
	
	email = forms.EmailField(required=True,widget=forms.EmailInput(attrs={'placeholder': 'Email','class' : 'form-control'}),label='Adresse Email')
	class Meta:
		model = Utilisateur
		fields = ['email']
	def validate_unique(self):
		pass
		

class EnregistrementForm(forms.ModelForm):
	email = forms.EmailField(required=True,widget=forms.EmailInput(attrs={'placeholder': 'Email','class' : 'form-control'}),label='Email')
	mot_passe = forms.CharField(required=True,widget=forms.PasswordInput(attrs={'placeholder': 'Mot de passe','class' : 'form-control'}),label='Mot de passe')
	pseudo = forms.CharField(required=True,widget=forms.TextInput(attrs={'placeholder': 'Pseudo','class' : 'form-control'}),label='Pseudo')
	pays = forms.CharField(required=True,widget=forms.TextInput(attrs={'placeholder': 'Pays','class' : 'form-control'}),label='Pays')
	ville = forms.CharField(required=True,widget=forms.TextInput(attrs={'placeholder': 'Ville','class' : 'form-control'}),label='Ville')
	date_naiss = forms.DateField(required=True,widget=forms.DateInput(attrs={'placeholder': 'Date','class' : 'form-control'}),label='Date de naissance')
	#date = forms.DateField(required=True,widget=SelectDateWidget(),label='Date de naissance')
	class Meta:
		model = Utilisateur
		fields = ['email','mot_passe','pseudo','pays','ville','date_naiss']
	

class Modif_profilForm(forms.ModelForm):
	email = forms.EmailField(required=True,widget=forms.EmailInput(attrs={'placeholder': 'Email','class' : 'form-control'}),label='Email')
	nom = forms.CharField(required=True,widget=forms.TextInput(attrs={'placeholder': 'Nom','class' : 'form-control'}),label='Nom')
	pays = forms.CharField(required=True,widget=forms.TextInput(attrs={'placeholder': 'Pays','class' : 'form-control'}),label='Pays')
	ville = forms.CharField(required=True,widget=forms.TextInput(attrs={'placeholder': 'Ville','class' : 'form-control'}),label='Ville')
	date_naiss = forms.DateField(required=True,widget=forms.DateInput(attrs={'placeholder': 'Date','class' : 'form-control'}),label='Date de naissance')
	photo  = forms.ImageField()
	class Meta:
		model = Utilisateur
		fields = ['nom','email','pays','ville','date_naiss','photo']

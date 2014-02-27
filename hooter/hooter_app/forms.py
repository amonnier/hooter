# coding = utf-8

from django import forms
from hooter_app.models import Utilisateur

class ConnexionForm(forms.ModelForm):
	
	email = forms.EmailField(required=True,widget=forms.EmailInput(attrs={'placeholder': 'Email'}),label='')
	mot_passe = forms.CharField(required=True,widget=forms.PasswordInput(attrs={'placeholder': 'Mot de passe'}),label='')
	class Meta:
		model = Utilisateur
		fields = ['email','mot_passe']
		
		

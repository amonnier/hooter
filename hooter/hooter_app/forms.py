# coding = utf-8

from django import forms
from hooter_app.models import Utilisateur

class ConnexionForm(forms.ModelForm):
	class Meta:
		model = Utilisateur
		#fields = ['email','mot_passe']
		email = forms.EmailField()
		mot_passe = forms.PasswordInput()

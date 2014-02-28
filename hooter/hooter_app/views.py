from django.shortcuts import redirect
from hooter_app.forms import ConnexionForm,EnregistrementForm
from hooter_app.models import Utilisateur
from django.shortcuts import render,get_object_or_404
from django.views.decorators.csrf import csrf_protect
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from hooter_app.models import Utilisateur, Message
# Create your views here.

def index(request):	
	formulaire = ConnexionForm()
	formEnregistrement = EnregistrementForm()
	contexte = {'formulaire':formulaire,'formEnregistrement':formEnregistrement,}
	return render(request, 'index.html',contexte)

@csrf_protect
def connexion(request):
	if 'email' in request.POST:
		formulaire=ConnexionForm(request.POST)
		contexte = {'formulaire':formulaire,}
		if formulaire.is_valid():
			try:
				utilisateur = Utilisateur.objects.get(email=formulaire.cleaned_data['email'],mot_passe=formulaire.cleaned_data['mot_passe'])
				return redirect('profile_view',utilisateur.pseudo)
			except Utilisateur.DoesNotExist:
				contexte['errors']='Utilisateur inconnu'
				return render(request, 'index.html',contexte)
		else:
			if 'email' in formulaire.errors:
				contexte['errors']="Adresse email incorrecte"
			if 'mot_passe' in formulaire.errors:
				contexte['errors']=contexte['errors']+', mot de passe vide'
			return render(request, 'index.html',contexte)
	else:
		return redirect('index')
		
def enregistrement(request):
	
	if 'email' in request.POST:
		enregistrement = EnregistrementForm(request.POST)#on remplit le formulaire
		
		if enregistrement.is_valid():
			nouvel_utilisateur = Utilisateur()
			nouvel_utilisateur.pseudo = enregistrement.cleaned_data['pseudo']
			nouvel_utilisateur.email = enregistrement.cleaned_data['email']
			nouvel_utilisateur.mot_passe = enregistrement.cleaned_data['mot_passe']
			nouvel_utilisateur.ville = enregistrement.cleaned_data['ville']
			nouvel_utilisateur.pays = enregistrement.cleaned_data['pays']
			nouvel_utilisateur.date_naiss = enregistrement.cleaned_data['date_naiss']
			
			nouvel_utilisateur.save()
			
			return HttpResponse("Registered!")
		else:
			return render(request, 'index.html',{'formEnregistrement':enregistrement,'formulaire':ConnexionForm()})
			
		 
	return HttpResponse("Register!")


def profile_view(request, pseudo):

	infos=get_object_or_404(Utilisateur, pseudo=pseudo)
	
	contexte={'infos' : infos}

	return render(request, 'profile_view.html',contexte)


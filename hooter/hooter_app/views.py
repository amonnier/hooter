# -*-coding:utf-8 -*
from django.shortcuts import redirect
from hooter_app.forms import ConnexionForm,EnregistrementForm,RecupPassForm, Modif_profilForm
from hooter_app.models import Utilisateur
from django.shortcuts import render,get_object_or_404
from django.views.decorators.csrf import csrf_protect
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from hooter_app.models import Utilisateur, Message
from django.conf import settings
from django.core.mail import send_mail

# Create your views here.

def index(request):	
	formulaire = ConnexionForm()
	formEnregistrement = EnregistrementForm()
	contexte = {'formulaire':formulaire,'formEnregistrement':formEnregistrement,}
	return render(request, 'index.html',contexte)
	
def recup_pass(request):
	if 'email' in request.POST:
		recup = RecupPassForm(request.POST)
		if recup.is_valid():
			try:
				utilisateur = Utilisateur.objects.get(email=recup.cleaned_data['email'])
				sujet = "Recuperation mot de passe - Hooter"
				corps = "Vous aviez perdu votre mot de passe. Le voici : %s"%utilisateur.mot_passe
				emetteur = "webmaster@hooter.com"
				destinataires = [utilisateur.email,]
				
				send_mail(sujet,corps,emetteur,destinataires)
				return render(request,'recuperation.html',{'formulaire_recuperation':recup,'succes':'Mot de passe envoyé avec succès!'})
			except Utilisateur.DoesNotExist:
				return render(request,'recuperation.html',{'formulaire_recuperation':recup,'errors':'Adresse mail non reconnue.'})
		else:
			
			render(request,'recuperation.html',{'formulaire_recuperation':recup,})
	
	else:
		recup = RecupPassForm()
	
	return render(request,'recuperation.html',{'formulaire_recuperation':recup,})

def deconnexion(request):
	request.session.flush()
	formulaire = ConnexionForm()
	formEnregistrement = EnregistrementForm()
	contexte = {'formulaire':formulaire,'formEnregistrement':formEnregistrement,}
	return render(request, 'index.html',contexte)
	


@csrf_protect
def connexion(request):
	if 'email' in request.POST:
		formulaire=ConnexionForm(request.POST)
		contexte = {'formulaire':formulaire,'formEnregistrement':EnregistrementForm()}
		if formulaire.is_valid():
			try:
				utilisateur = Utilisateur.objects.get(email=formulaire.cleaned_data['email'],mot_passe=formulaire.cleaned_data['mot_passe'])
				
				request.session['pseudo']=utilisateur.pseudo
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


@csrf_protect		
def enregistrement(request):
	
	if 'email' in request.POST:
		enregistrement = EnregistrementForm(request.POST)#on remplit le formulaire
		
		if enregistrement.is_valid():
			nouvel_utilisateur = Utilisateur()
			nouvel_utilisateur.pseudo = enregistrement.cleaned_data['pseudo']
			nouvel_utilisateur.nom = enregistrement.cleaned_data['pseudo']
			nouvel_utilisateur.email = enregistrement.cleaned_data['email']
			nouvel_utilisateur.mot_passe = enregistrement.cleaned_data['mot_passe']
			nouvel_utilisateur.ville = enregistrement.cleaned_data['ville']
			nouvel_utilisateur.pays = enregistrement.cleaned_data['pays']
			nouvel_utilisateur.date_naiss = enregistrement.cleaned_data['date_naiss']
			
			nouvel_utilisateur.save()
			
			return render(request,'index.html',{'formEnregistrement':EnregistrementForm(),'formulaire':ConnexionForm(),'succes':'Enregistrement réussi ! Connectez-vous.',})
		else:
			return render(request, 'index.html',{'formEnregistrement':enregistrement,'formulaire':ConnexionForm()})
			
		 
	return HttpResponse("Register!")


def profile_view(request, pseudo):
	if 'pseudo' in request.session:
		infos=get_object_or_404(Utilisateur, pseudo=pseudo)
	
		contexte={'infos' : infos}
		
		return render(request, 'profile_view.html',contexte)
	else:
		return redirect('index')

@csrf_protect
def modif_profil(request, pseudo):
	if 'pseudo' in request.session:

		utilisateur=get_object_or_404(Utilisateur, pseudo=pseudo)
		formulaire=Modif_profilForm(instance=utilisateur)
		
		contexte={'utilisateur' : utilisateur, 'form':formulaire}

		return render(request, 'modif_profil.html',contexte)
	
	else:
		return redirect('index')
		
@csrf_protect
def enregistrer_profil(request):

	utilisateur2=get_object_or_404(Utilisateur, pseudo=request.session['pseudo'])
	formulaire2=Modif_profilForm(request.POST,request.FILES, instance=utilisateur2)
		
	contexte={'utilisateur' : utilisateur2, 'form':formulaire2}

	if 'POST' in request.method:
		if formulaire2.is_valid():
			formulaire2.save()
			
			return profile_view(request,request.session['pseudo'])
		else:
			return modif_profil(request,request.session['pseudo'])		
	else:
		return redirect(request.session['pseudo'],'/settings')


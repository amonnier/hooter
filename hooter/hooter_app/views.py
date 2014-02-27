from django.shortcuts import redirect
from hooter_app.forms import ConnexionForm
from hooter_app.models import Utilisateur
from django.shortcuts import render,get_object_or_404
from django.views.decorators.csrf import csrf_protect
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from hooter_app.models import Utilisateur
# Create your views here.

def index(request):	
	formulaire = ConnexionForm()
	contexte = {'formulaire':formulaire,}
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
			
			return render(request, 'index.html',contexte)
	else:
		return redirect('index')
		
	


def profile_view(request, pseudo):
	u = Utilisateur.objects.get(pseudo=pseudo)
	infos=get_object_or_404(Utilisateur, pseudo=u)
	contexte={'infos' : infos}
	return render(request, 'profile_view.html',contexte)


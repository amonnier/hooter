
from hooter_app.forms import ConnexionForm
from django.shortcuts import render,get_object_or_404

from django.http import HttpResponse
from hooter_app.models import Utilisateur
# Create your views here.

def index(request):	
	formulaire = ConnexionForm(request.POST)
	contexte = {'formulaire':formulaire,}
	return render(request, 'index.html',contexte)



def profile_view(request, pseudo):
	u = Utilisateur.objects.get(pseudo=pseudo)
	infos=get_object_or_404(Utilisateur, pseudo=u)
	contexte={'infos' : infos}
	return render(request, 'profile_view.html',contexte)


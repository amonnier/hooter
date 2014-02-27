from django.shortcuts import render
from hooter_app.forms import ConnexionForm

# Create your views here.

def index(request):
	
	formulaire = ConnexionForm(request.POST)
	contexte = {'formulaire':formulaire,}
	return render(request, 'index.html',contexte)

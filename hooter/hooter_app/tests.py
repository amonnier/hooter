from django.test import TestCase
from hooter_app.models import Utilisateur
# Create your tests here.

class UtilisateurTestCase(TestCase):
    def setUp(self):
        Utilisateur.objects.create(pseudo="UtilisateurTest",nom="UtilisateurTest",mot_passe="toto",email="utilisateur@email.com",pays="totopays",ville="totoville",date_naiss="1990-04-03")
        

	def test_creation_utilisateur(self):
		user = Utilisateur.objects.get(pseudo="UtilisateurTest")

		self.assertEquals(user.ville,"totoville")


		#test de l'unicite du pseudo
		assertEquals(creation_utilisateur("UtilisateurTest","test","test","test@email.com","test","test","1990-04-03"),False)
		

	def creation_utilisateur(pseudo,nom,mot_passe,email,pays,ville,date_naiss):
		try:
			Utilisateur.objects.create(pseudo,nom,mot_passe,email,pays,ville,date_naiss)
			return True
		except IntegrityError:
			return False

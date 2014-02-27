from django.contrib import admin
from hooter_app.models import Utilisateur, Message, Hashtag



class UtilisateurAdmin(admin.ModelAdmin):
	search_fields=['pseudo']



# Register your models here.
admin.site.register(Utilisateur, UtilisateurAdmin)
admin.site.register(Message)
admin.site.register(Hashtag)

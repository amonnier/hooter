from django.contrib import admin
from hooter_app.models import Utilisateur, Message, Hashtag
# Register your models here.
admin.site.register(Utilisateur)
admin.site.register(Message)
admin.site.register(Hashtag)

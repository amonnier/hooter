from django import template
from django.core.urlresolvers import reverse
import re

register = template.Library()


@register.filter(name="make_url_to_profile_and_hashtag")
def name_to_profile_and_hashtags_url(value):
	
	message_split= value.replace('.',' ').replace('!',' ').split(" ")
	for word in message_split:
		mot_original=word
		#cas ou c'est un appel d'un autre utilisateur
		if '@' in word:

			value = value.replace(word,"<a href=\"%s\">%s</a>"%(reverse('profile_view', args=[word.replace("@","")]),word))
		#cas ou c'est un appel d'un hashtag
		if '#' in word:
			if word.replace('#','') != '':
				hashtag = word
				
				for char in hashtag:#on remplace tous les eventuels caracteres avant le #
					if char == "#":
						break
					else:
						hashtag = hashtag.replace(char,'',1)
				#on enleve les caracteres speciaux pouvant se trouver a la fin du mot
				for char in ',!;:./?*$\'"':
					word=word.replace(char,'')
				#on enleve le # pour une utilisation dans l'url
				
				tampon=hashtag
				for char in ',!;:./?*$\'"':#on enleve au hashtag tout caractere special
					tampon.replace(char,'')
				
				#le hashtag a afficher dans l'url
				message_url = word.replace(mot_original.replace(tampon,'',1),'',1)
				message_url = message_url.replace('#','')
				
				message_avant = mot_original.replace(tampon,'')
				
				value = value.replace(mot_original,"%s<a href=\"%s\">%s</a>"%(message_avant,reverse('afficher_hashtag_full', args=[message_url]),hashtag))
	
	return value

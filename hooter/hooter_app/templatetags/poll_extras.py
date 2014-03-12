from django import template
from django.core.urlresolvers import reverse

register = template.Library()


@register.filter(name="make_url_to_profile_and_hashtag")
def name_to_profile_and_hashtags_url(value):
	
	message_split= value.split(" ")
	for word in message_split:
		#cas ou c'est un appel d'un autre utilisateur
		if '@' in word:

			value = value.replace(word,"<a href=\"%s\">%s</a>"%(reverse('profile_view', args=[word.replace("@","")]),word))
		#cas ou c'est un appel d'un hashtag
		if '#' in word:
			
			hashtag = word
			for char in hashtag:#on remplace tous les eventuels caracteres avant le #
				if char == "#":
					break
				else:
					hashtag = hashtag.replace(char,'',1)
			#on enleve le # pour une utilisation dans l'url
			value = value.replace(word,"%s<a href=\"%s\">%s</a>"%(word.replace(hashtag,''),reverse('afficher_hashtag_full', args=[hashtag.replace('#','')]),hashtag))
	
	return value

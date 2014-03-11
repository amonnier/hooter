from django import template
from django.core.urlresolvers import reverse

register = template.Library()


@register.filter(name="make_url_to_profile")
def name_to_profile_url(value):
	
	message_split= value.split(" ")
	for word in message_split:
		if '@' in word:
			
			utilisateur = word.replace('@','')
			value = value.replace(word,"<a href=\"%s\">%s</a>"%(reverse('profile_view', args=[word.replace("@","")]),word))
	
	return value

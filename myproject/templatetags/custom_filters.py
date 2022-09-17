from django.template.defaulttags import register


@register.filter
def get_from_dictionary(dictionary, key):
   return dictionary.get(key)

@register.filter
def is_user_choice(dictionary, key):
   return dictionary.get(key).get('is_user_choice')
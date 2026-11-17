"""Contact details shown in the footer and on several pages. Change them here only."""

SITE_CONTACT = {
    'phone_display': '+31 06 42781591',
    'phone_link': '+31642781591',
    'email': 'moonen.peggy@gmail.com',
    'location': 'Beekdaelen, Limburg',
    # TODO: replace with the real profile URLs
    'instagram_url': 'https://www.instagram.com/',
    'facebook_url': 'https://www.facebook.com/',
}


def site_contact(request):
    return {'site': SITE_CONTACT}

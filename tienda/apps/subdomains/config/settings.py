
from django.conf import settings

BASE_DOMAIN = getattr(settings, 'BASE_DOMAIN', 'test.com')
UNALLOWED_SUBDOMAINS = getattr(settings, 'UNALLOWED_SUBDOMAINS', ['www', 'shabda'])

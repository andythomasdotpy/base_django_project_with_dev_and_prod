from decouple import config

from .base import *


print("prod")
SECRET_KEY = config("DJANGO_SECRET_KEY")
DEBUG = False
ALLOWED_HOSTS = [
    "eb-dev-and-prod-settings-env.eba-akljfkeifeja.us-west-2.elasticbeanstalk.com", 
    "127.0.0.1",
    "example.com",
    "www.example.com",
    ]

## All 5 below false when deploying. If True, issues testing in browser. You can remove cookie and hard reset or close ingonito browser.
## Swith to True after deployment successful
# HTTPS settings
SESSION_COOKIE_SECURE = False
CSRF_COOKIE_SECURE = False
SECURE_SSL_REDIRECT = False


# HSTS settings
SECURE_HSTS_SECONDS = 31536000 # 1 year
SECURE_HSTS_PRELOAD = False
SECURE_HSTS_INCLUDE_SUBDOMAINS = False
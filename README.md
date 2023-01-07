# Deployment Checklist

1) Change .ebextensions/django.config WSGIPath: ###########.wsgi:application to project name
2) prod.py HSTS and HTTPS settings all false for test deploy. Change to True
3) Variable "USER" not accepted for database info in settings/base.py 
4) "Allowed Hosts" updated in settings/prod.py. CNAME and local ip before SSL cert. example.com and www.example.com after SSL cert.

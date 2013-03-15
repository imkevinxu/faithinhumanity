import os, site, sys

# From http://jmoiron.net/blog/deploying-django-mod-wsgi-virtualenv/

vepath = '/home/ubuntu/.virtualenvs/faithinhumanity/lib/python2.7/site-packages'

prev_sys_path = list(sys.path)

site.addsitedir(vepath)

sys.path.append('/home/ubuntu/django_projects')
sys.path.append('/home/ubuntu/django_projects/faithinhumanity')
sys.path.append('/home/ubuntu/django_projects/faithinhumanity/faithinhumanity_site')

# reorder sys.path so new directories from the addsitedir show up first
new_sys_path = [p for p in sys.path if p not in prev_sys_path]
for item in new_sys_path:
    sys.path.remove(item)
sys.path[:0] = new_sys_path

from django.core.handlers.wsgi import WSGIHandler
os.environ['DJANGO_SETTINGS_MODULE'] = 'faithinhumanity.settings'
application = WSGIHandler()
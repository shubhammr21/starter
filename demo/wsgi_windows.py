from django.core.wsgi import get_wsgi_application
import site
import sys
import os
activate_this = 'G:/_envs/starter/Scripts/activate'
# execfile(activate_this, dict(__file__=activate_this))
exec(open(activate_this).read(), dict(__file__=activate_this))


# Add the site-packages of the chosen virtualenv to work with
site.addsitedir('G:/_envs/starter/lib/site-packages')


# Add the app's directory to the PYTHONPATH
sys.path.append('G:/Aabhyasa/starter')
sys.path.append('G:/Aabhyasa/starter/demo')

os.environ['DJANGO_SETTINGS_MODULE'] = 'demo.settings'
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "demo.settings")

application = get_wsgi_application()

from django.http import HttpResponse
from django.template import loader
from .models import Ship_params

def shipparams(request):
  myships = Ship_params.objects.all().values()
  template = loader.get_template('all_ship.html')
  context = {
    'myships': myships,
  }
  return HttpResponse(template.render(context, request))
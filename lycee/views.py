from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Cursus
from django.template import loader


def detail(request,cursus_id):
  resp='result for cursus {}'.format(cursus_id)
  return HttpResponse(resp)

def index(request):
  result_list = Cursus.objects.order_by('name')
  #chargement du template
  template=loader.get_template('lycee/index.html')

  #context
  context = {
    'liste' : result_list,
  }
  return HttpResponse(template.render(context,request))


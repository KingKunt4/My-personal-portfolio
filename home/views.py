from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import devices
def welcome(request):
    template = loader.get_template('home_page.html')
    return HttpResponse(template.render())

def Devices(request):
    all_devices = devices.objects.all().values()
    template = loader.get_template('devices.html')
    relation = {
        'devices': all_devices,
    }
    return HttpResponse(template.render(relation, request))
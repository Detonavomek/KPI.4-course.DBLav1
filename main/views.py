from django.shortcuts import render
from django.http import HttpResponse
from models import Account, Pet

from datetime import datetime


def index(request):
    # pet = Pet()
    pet = Pet.get(5)
    # pet.params['name'] = 'newfsdf6213'
    # pet.params['age'] = '444'
    # pet.params['specie'] = 'new_sp_44421'
    pet.save()
    pet.delete()
    return HttpResponse('OK')

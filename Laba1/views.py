from django.shortcuts import render
from django.http import HttpResponse
from models import Account, Pet

from datetime import datetime

def index(request):
	# account_data = {
	# 	'amount': 122,
	# 	'manager': 'asjfpoi',
	# 	'dateCreating': datetime.now(),
	# }
	# account = Account(account_data)

	pet_data = {
		'name': 'pet name 1',
		'age': 34,
		'specie': 'sold',
	}
	pet = Pet(pet_data)
	pet.insert()
	# account.manager = 'qwerty123'
	# account.insert()
	return HttpResponse('OK')

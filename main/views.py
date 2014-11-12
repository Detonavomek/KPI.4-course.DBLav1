from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import render_to_string

import json
import models

from forms import AddForm


def add(request):
    form = AddForm(request.POST or None)
    if form.is_valid():
        # add object
        data = {
            "status": "ok",
            "next_url": '/',
        }
    else:
        context = {'form': form, }
        html = render_to_string('main/form.html', context)
        data = {
            "status": 'invalid',
            "html": html
        }
    return HttpResponse(json.dumps(data), content_type="application/json")


def home(request):
    # for i in range(1, 9):
    #     pet = models.Table3()
    # pet = Pet.get(5)
    #     pet.params['table1_id'] = str(i)
    #     pet.params['table2_id'] = str(9 - i)
    #     pet.params['field5'] = 'field5_' + str(i)
    #     pet.save()
    # pet.delete()
    return render(request, 'main/home.html', {"rows": models.main_table.get_all()})
    return HttpResponse('OK')
